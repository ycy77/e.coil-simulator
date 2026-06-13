---
entity_id: "complex.ecocyc.CPLX0-8576"
entity_type: "complex"
name: "DNA-binding transcriptional repressor FrlR"
source_database: "EcoCyc"
source_id: "CPLX0-8576"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# DNA-binding transcriptional repressor FrlR

`complex.ecocyc.CPLX0-8576`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-8576`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P45544|protein.P45544]]

## Enriched Summary

As a dimer, FrlR binds DNA to regulate transcription, and it becomes inactive as a regulator when it is bound to fructoselysine-6-phosphate . It has a winged helix-turn-helix domain for binding DNA, and this domain contains the amino acids Arg49, Gly70, and Lys71, which appear to be essential for DNA binding . FrlR has similarity to Bacillus subtilis FrlR , B. subtilis NagR , and S. enterica FraR . As homologues, this protein appears to pertain to the GntR/HutC family of transcriptional regulators . It appears that the frlR gene undergoes adaptive mutations when E. coli invades a mammalian host . The FrlR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . FrlR: fructolysine As a dimer, FrlR binds DNA to regulate transcription, and it becomes inactive as a regulator when it is bound to fructoselysine-6-phosphate . It has a winged helix-turn-helix domain for binding DNA, and this domain contains the amino acids Arg49, Gly70, and Lys71, which appear to be essential for DNA binding . FrlR has similarity to Bacillus subtilis FrlR , B...

## Biological Role

Component of FrlR- N6-(1-deoxy-6-O-phospho-D-fructos-1-yl)-L-lysine (complex.ecocyc.CPLX0-8577).

## Annotation

As a dimer, FrlR binds DNA to regulate transcription, and it becomes inactive as a regulator when it is bound to fructoselysine-6-phosphate . It has a winged helix-turn-helix domain for binding DNA, and this domain contains the amino acids Arg49, Gly70, and Lys71, which appear to be essential for DNA binding . FrlR has similarity to Bacillus subtilis FrlR , B. subtilis NagR , and S. enterica FraR . As homologues, this protein appears to pertain to the GntR/HutC family of transcriptional regulators . It appears that the frlR gene undergoes adaptive mutations when E. coli invades a mammalian host . The FrlR binding landscape was globally mapped in vivo by standardized ChIP-seq and quantitatively modeled using BoltzNet, a biophysically informed neural network that infers binding energy from sequence data . The resulting ChIP-seq binding regions are available in RegulonDB (Galagan collection), and the corresponding energy matrix and genomic binding profiles can be accessed at boltznet.bu.edu . FrlR: fructolysine

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8577|complex.ecocyc.CPLX0-8577]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `is_component_of` <-- [[protein.P45544|protein.P45544]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## External IDs

- `EcoCyc:CPLX0-8576`
- `QSPROTEOME:QS00195205`

## Notes

2*protein.P45544
