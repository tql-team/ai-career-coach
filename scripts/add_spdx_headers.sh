#!/usr/bin/env bash
# SPDX-License-Identifier: MIT
# Script tự động quét và thêm SPDX-License-Identifier: MIT vào toàn bộ file .py và .js

set -e

for f in $(find . -name "*.py" -not -path "./.git/*" -not -path "./venv/*" -not -path "./.venv/*"); do
    if ! grep -q "SPDX-License-Identifier" "$f"; then
        tmp=$(mktemp)
        printf "# SPDX-License-Identifier: MIT\n" > "$tmp"
        cat "$f" >> "$tmp"
        mv "$tmp" "$f"
        echo "Added SPDX header to $f"
    fi
done

for f in $(find . -name "*.js" -not -path "./.git/*" -not -path "./node_modules/*"); do
    if ! grep -q "SPDX-License-Identifier" "$f"; then
        tmp=$(mktemp)
        printf "// SPDX-License-Identifier: MIT\n" > "$tmp"
        cat "$f" >> "$tmp"
        mv "$tmp" "$f"
        echo "Added SPDX header to $f"
    fi
done

echo "Hoàn tất kiểm tra và bổ sung SPDX-License-Identifier: MIT cho toàn bộ mã nguồn!"
