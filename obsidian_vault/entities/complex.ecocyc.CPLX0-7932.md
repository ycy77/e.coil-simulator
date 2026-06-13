---
entity_id: "complex.ecocyc.CPLX0-7932"
entity_type: "complex"
name: "cytosine/isoguanine deaminase"
source_database: "EcoCyc"
source_id: "CPLX0-7932"
default_state: "active"
allowed_states: "active|impaired|disrupted|assembled|disassembled|inhibited"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/complex
  - source/EcoCyc
aliases:
---

# cytosine/isoguanine deaminase

`complex.ecocyc.CPLX0-7932`

## Static

- Type: `complex`
- Source: `EcoCyc:CPLX0-7932`
- Default state: `active`
- Allowed states: `active|impaired|disrupted|assembled|disassembled|inhibited`
- Complex type: `regulatory`
- Components: [[protein.P25524|protein.P25524]]

## Enriched Summary

Cytosine deaminase (CDA) is an enzyme in the pyrimidine salvage pathway, catalyzing the deamination of cytosine to uracil, which allows the cell to utilize cytosine for pyrimidine nucleotide synthesis . It was more recently shown to catalyze deamination of isoguanine, a mutagenic oxidation product of adenine . As a mononuclear iron enzyme, CDA is damaged by micromolar hydrogen peroxide both in vitro and in vivo. Iron sequestration and substitution of Mn2+ for the Fe2+ cofactor can protect the enzyme . Earlier characterization of the enzyme had found it to consist of two polypeptides of different molecular mass . Later studies did not confirm this observation, finding only a single polypeptide . Crystal structures of wild-type and mutant CodA have been solved . The enzyme is in a hexameric domain-swapped β-barrel conformation with the active site located at the barrel opening . Random and site-directed mutagenesis has been used to identify active site residues and mutants that are more active with 5-fluorocytosine as substrate . A reaction mechanism has been proposed . Expression of CodA is repressed by the presence of pyrimidine nucleobases in the medium and increased by growth on poor nitrogen sources . The transcription start site and subsequent elongation to a full codBA mRNA is regulated by the level of UTP . Regulation is reviewed in...

## Biological Role

Catalyzes CYTDEAM-RXN (reaction.ecocyc.CYTDEAM-RXN), RXN0-6708 (reaction.ecocyc.RXN0-6708). Bound by Fe2+ (molecule.C14818).

## Annotation

Cytosine deaminase (CDA) is an enzyme in the pyrimidine salvage pathway, catalyzing the deamination of cytosine to uracil, which allows the cell to utilize cytosine for pyrimidine nucleotide synthesis . It was more recently shown to catalyze deamination of isoguanine, a mutagenic oxidation product of adenine . As a mononuclear iron enzyme, CDA is damaged by micromolar hydrogen peroxide both in vitro and in vivo. Iron sequestration and substitution of Mn2+ for the Fe2+ cofactor can protect the enzyme . Earlier characterization of the enzyme had found it to consist of two polypeptides of different molecular mass . Later studies did not confirm this observation, finding only a single polypeptide . Crystal structures of wild-type and mutant CodA have been solved . The enzyme is in a hexameric domain-swapped β-barrel conformation with the active site located at the barrel opening . Random and site-directed mutagenesis has been used to identify active site residues and mutants that are more active with 5-fluorocytosine as substrate . A reaction mechanism has been proposed . Expression of CodA is repressed by the presence of pyrimidine nucleobases in the medium and increased by growth on poor nitrogen sources . The transcription start site and subsequent elongation to a full codBA mRNA is regulated by the level of UTP . Regulation is reviewed in . Cytosine deaminase is present in prokaryotes and fungi, but not in multicellular eukaryotes. It is thus of interest for the design of antimicrobial agents. Cytosine deaminase is also being used for suicide gene therapy against tumors, e.g. .

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.CYTDEAM-RXN|reaction.ecocyc.CYTDEAM-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-6708|reaction.ecocyc.RXN0-6708]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `is_component_of` <-- [[protein.P25524|protein.P25524]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## External IDs

- `EcoCyc:CPLX0-7932`
- `QSPROTEOME:QS00181829`

## Notes

6*protein.P25524
