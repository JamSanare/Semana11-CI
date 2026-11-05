# Uso: bash scripts/gate_k6.sh <log> <nombre>
# Muestra el resultado por escenario y falla si alguno incumple umbral (99) o el servidor cae.
LOG="$1"; NOMBRE="${2:-k6}"; FALLOS=0; ESC=""
while IFS= read -r l; do
  case "$l" in
    "=== "*) ESC="$l" ;;
    *"código de salida: 0"*) echo "OK     $ESC" ;;
    *"código de salida: "*) echo "FALLA  $ESC -> $l"; FALLOS=$((FALLOS+1)) ;;
    *"servidor: CAÍDO"*) echo "CAIDO  $ESC"; FALLOS=$((FALLOS+1)) ;;
  esac
done < "$LOG"
echo "[$NOMBRE] escenarios con hallazgo: $FALLOS"
[ "$FALLOS" -eq 0 ]
