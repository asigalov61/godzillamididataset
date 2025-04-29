# Godzilla MIDI Dataset
## Enormous, comprehensive, normalized and searchable MIDI dataset for MIR and symbolic music AI purposes

![Godzilla-MIDI-Dataset](https://github.com/user-attachments/assets/8008d578-f120-4a02-a0bf-7154e9a7423d)

***

## Dataset features

### 1) Over 5.43M+ unique, de-duped and normalized MIDIs
### 2) Each MIDI was converted to proper MIDI format specification and checked for integrity
### 3) Dataset was de-duped twice: by md5 hashes and by pitches-patches counts
### 4) Extensive and comprehansive (meta)data was collected from all MIDIs in the dataset
### 5) Dataset comes with a custom-designed and highly optimized GPU-accelerated search and filter code

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

## Quick-start use example

```python
# Import main Godzilla MIDI Dataset module
import godzillamididataset

# Download Godzilla MIDI Dataset from Hugging Face repo
godzillamididataset.donwload_dataset()

# Extract Godzilla MIDI Dataset with built-in function (slow)
godzillamididataset.parallel_extract()

# Or you can extract much faster if you have installed the optional packages for Fast Parallel Extract
# from godzillamididataset import fast_parallel_extract
# fast_parallel_extract.fast_parallel_extract()

# Load all MIDIs basic signatures
sigs_data = godzillamididataset.read_jsonl()

# Create signatures dictionaries
sigs_dicts = godzillamididataset.load_signatures(sigs_data)

# Pre-compute signatures
X, global_union = godzillamididataset.precompute_signatures(sigs_dicts)

# Run the search
# IO dirs will be created on the first run of the following function
# Do not forget to put your master MIDIs into created Master-MIDI-Dataset folder
# The full search for each master MIDI takes about 2-3 sec on a GPU and 4-5 min on a CPU
godzillamididataset.search_and_filter(sigs_dicts, X, global_union)
```

***

## Dataset structure information

```
Godzilla-MIDI-Dataset/
├── ARTWORK/                    # Concept artwork
│   ├── Illustrations/          # Concept illustrations
│   ├── Logos/                  # Dataset logos
│   └── Posters/                # Dataset posters
├── CODE/                       # Supplemental python code and python modules
├── DATA/                       # Dataset (meta)data dir
│   ├── Averages/               # Averages data for all MIDIs and clean MIDIs
│   ├── Basic Features/         # All basic features for all clean MIDIs
│   ├── Files Lists/            # Files lists by MIDIs types and categories
│   ├── Identified MIDIs/       # Comprehensive data for identified MIDIs
│   ├── Metadata/               # Raw metadata from all MIDIs
│   ├── Mono Melodies/          # Data for all MIDIs with monophonic melodies
│   ├── Pitches Patches Counts/ # Pitches-patches counts for all MIDIs 
│   ├── Pitches Sums/           # Pitches sums for all MIDIs
│   ├── Signatures/             # Signatures data for all MIDIs and MIDIs subsets
│   └── Text Captions/          # Music description text captions for all MIDIs
├── MIDIs/                      # Root MIDIs directory
└── SOUNDFONTS/                 # Select high-quality soundfont banks to render MIDIs
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
