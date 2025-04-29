# [WIP] Godzilla MIDI Dataset
## Enormous, comprehensive, normalized and searchable MIDI dataset for MIR and symbolic music AI purposes

![Godzilla-MIDI-Dataset](https://github.com/user-attachments/assets/8008d578-f120-4a02-a0bf-7154e9a7423d)

***

## Installation

### pip and setuptools

```sh
# It is recommended that you upgrade pip and setuptools prior to install for max compatibility
!pip install --upgrade pip
!pip install --upgrade setuptools
```

### CPU-only install

```sh
# The following command will install Godzilla MIDI Dataset for CPU-only search
# Please note that CPU search is quite slow and it requires a minimum of 128GB RAM to work for full searches

!pip install -U godzillamididataset
```

### CPU/GPU install

```sh
# The following command will install Godzilla MIDI Dataset for fast GPU search
# Please note that GPU search requires at least 80GB GPU VRAM for full searches

!pip install -U godzillamididataset[gpu]
```

### Optional packages

#### Packages for Fast Parallel Exctract module

```sh
# The following command will install packages for Fast Parallel Extract module
# It will allow you to extract (untar) Godzilla MIDI Dataset much faster

!sudo apt update -y
!sudo apt install -y p7zip-full
!sudo apt install -y pigz
```

#### Packages for midi_to_colab_audio module

```sh
# The following command will install packages for midi_to_colab_audio module
# It will allow you to render Godzilla MIDI Dataset MIDIs to audio

!sudo apt update -y
!sudo apt install fluidsynth
```

***

## Citation card

```bibtex
@misc{GodzillaMIDIDataset2025,
  title        = {Godzilla MIDI Dataset: Enormous, comprehensive, normalized and searchable MIDI dataset for MIR and symbolic music AI purposes},
  author       = {Alex Lev},
  publisher    = {Project Los Angeles / Tegridy Code},
  year         = {2025},
  url          = {https://huggingface.co/datasets/projectlosangeles/Godzilla-MIDI-Dataset}
```

***

### Project Los Angeles
### Tegridy Code 2025
