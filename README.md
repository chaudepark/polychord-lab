# Polychord Lab

**https://chaudepark.github.io/polychord-lab/**

An explorer for hybrid / polychords: stack two triads (slash chords like `D/C`) and see the extended chord they produce — actual notes and degrees always computed, never just symbol lookup. Search forward (build a stack) or backward (from a chord name, a colour/degree, an upper triad, a mode, or the song's key).

This is one half of a two-app pair designed to be used side-by-side in browser split view:

| App | Role |
|---|---|
| [**Best Sub Bass Notes**](https://github.com/chaudepark/scale-reference) | Decide the song's foundation — key, sub note, modulation plan |
| **Polychord Lab** (this repo) | Refine the colour — extended voicings from stacked triads |

The two apps sync through same-origin `localStorage` (see below), so a key chosen in the sub-bass tool is picked up here live.

## Features

- One "current voicing" hero panel: slash spelling, derived chord symbol, mode, key-fit check, keyboard view, notes & degrees coloured by lower / upper / shared
- Eight ways in: by key (degree-grouped in-key voicings), build, by colour (degrees), by chord name, by upper triad (fixed top, moving bass — with **voice-leading badges**: shared / new pitch classes vs the current voicing), modulation (pivot in colour, common-bass pedal, reinterpretation of the current pitch-set), by mode, full table
- Audition via Web Audio, or through a **MIDI output** (e.g. the macOS IAC bus into Ableton) to hear voicings with your own sounds; spacebar replays
- **MIDI file export** of the current voicing (click to download, drag into the DAW on Chromium)
- **MIDI input**: held keys highlighted, played chord named, ✓ match against the current voicing, and "load this chord" to pull the nearest voicing in the system into the hero
- **Sketch loop**: collect voicings into a bottom bar (max 8 slots), loop at a chosen BPM, export the whole progression as MIDI. Shared live with the sub-bass tool.
- EN / 日本語

## 日本語

トライアド2つの積み（スラッシュ／ポリコード）から拡張和音の色を探すツールです。構成音と度数は常に実音から計算して表示します。組み立て・コード名・度数（色）・上トライアド・モード・キー・転調と、複数の入口から逆引きできます。

ブラウザのSplit viewで [Best Sub Bass Notes](https://github.com/chaudepark/scale-reference) と並べて使う前提の2アプリ構成です。**サブベースツールで曲の土台（キー）を決め、こちらで響きの色とボイシングを詰めます。** キー・言語・スケッチループは `localStorage` 経由でリアルタイムに連動します。

試聴は内蔵シンセのほか、MIDI出力（IAC Bus経由でAbletonなど）に切り替えて実際の音色で確認できます。MIDI鍵盤で弾いた響きの判定・取り込み、現在のボイシングや進行（スケッチループ）のMIDIファイル書き出しに対応。スペースキーで再試聴できます。

## Development

- Single static file: all data, logic and i18n live in `index.html` (the `DATA` voicing table, `I18N` for EN/JA). `verify.py` cross-checks the theory table.
- `localStorage` contract shared with the sub-bass tool (same origin):
  - `subbass-key` — `"<rootPc>|<scaleIndex>"`, read on load and followed live via `storage` events
  - `subbass-lang` — `"en" | "ja"`
  - `subbass-sketch` — JSON `{v, slots:[{label, mids:[midi…]}], bpm}` for the shared sketch loop
  - `polychord-midi-dev` / `polychord-midi-out` — remembered MIDI input / output device ids
