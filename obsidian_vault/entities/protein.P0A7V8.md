---
entity_id: "protein.P0A7V8"
entity_type: "protein"
name: "rpsD"
source_database: "UniProt"
source_id: "P0A7V8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsD ramA b3296 JW3258"
---

# rpsD

`protein.P0A7V8`

## Static

- Type: `protein`
- Source: `UniProt:P0A7V8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of two assembly initiator proteins for the 30S subunit, it binds directly to 16S rRNA where it nucleates assembly of the body of the 30S subunit. {ECO:0000269|PubMed:2461734}.; FUNCTION: With S5 and S12 plays an important role in translational accuracy; many suppressors of streptomycin-dependent mutants of protein S12 are found in this protein, some but not all of which decrease translational accuracy (ram, ribosomal ambiguity mutations).; FUNCTION: Plays a role in mRNA unwinding by the ribosome, possibly by forming part of a processivity clamp. {ECO:0000269|PubMed:15652481}.; FUNCTION: Protein S4 is also a translational repressor protein, it controls the translation of the alpha-operon (which codes for S13, S11, S4, RNA polymerase alpha subunit, and L17) by binding to its mRNA. {ECO:0000269|PubMed:3309351}.; FUNCTION: Also functions as a rho-dependent antiterminator of rRNA transcription, increasing the synthesis of rRNA under conditions of excess protein, allowing a more rapid return to homeostasis. Binds directly to RNA polymerase. {ECO:0000269|PubMed:11447122}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP)...

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of two assembly initiator proteins for the 30S subunit, it binds directly to 16S rRNA where it nucleates assembly of the body of the 30S subunit. {ECO:0000269|PubMed:2461734}.; FUNCTION: With S5 and S12 plays an important role in translational accuracy; many suppressors of streptomycin-dependent mutants of protein S12 are found in this protein, some but not all of which decrease translational accuracy (ram, ribosomal ambiguity mutations).; FUNCTION: Plays a role in mRNA unwinding by the ribosome, possibly by forming part of a processivity clamp. {ECO:0000269|PubMed:15652481}.; FUNCTION: Protein S4 is also a translational repressor protein, it controls the translation of the alpha-operon (which codes for S13, S11, S4, RNA polymerase alpha subunit, and L17) by binding to its mRNA. {ECO:0000269|PubMed:3309351}.; FUNCTION: Also functions as a rho-dependent antiterminator of rRNA transcription, increasing the synthesis of rRNA under conditions of excess protein, allowing a more rapid return to homeostasis. Binds directly to RNA polymerase. {ECO:0000269|PubMed:11447122}.; FUNCTION: Part of the processive rRNA transcription and antitermination complex (rrnTAC). The complex forms an RNA-chaperone ring around the RNA exit tunnel of RNA polymerase (RNAP). It supports rapid transcription and antitermination of rRNA operons, cotranscriptional rRNA folding, and annealing of distal rRNA regions to allow correct ribosome biogenesis. This subunit may play a particular role in long-distance rRNA annealing needed for pre-rRNA processing. {ECO:0000269|PubMed:32871103}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (5)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b3294|gene.b3294]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b3296|gene.b3296]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b3297|gene.b3297]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation
- `represses` --> [[gene.b3298|gene.b3298]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## Incoming Edges (1)

- `encodes` <-- [[gene.b3296|gene.b3296]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7V8`
- `KEGG:ecj:JW3258;eco:b3296;ecoc:C3026_17920;`
- `GeneID:86862306;93778691;947793;`
- `GO:GO:0000028; GO:0000900; GO:0002181; GO:0003735; GO:0005737; GO:0005829; GO:0006353; GO:0015935; GO:0019843; GO:0022627; GO:0031564; GO:0042274; GO:0045947; GO:0046677; GO:0048027; GO:1990145`

## Notes

Small ribosomal subunit protein uS4 (30S ribosomal protein S4)
