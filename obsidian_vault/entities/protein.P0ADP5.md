---
entity_id: "protein.P0ADP5"
entity_type: "protein"
name: "bioP"
source_database: "UniProt"
source_id: "P0ADP5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|Ref.5}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bioP yigM b3827 JW3803"
---

# bioP

`protein.P0ADP5`

## Static

- Type: `protein`
- Source: `UniProt:P0ADP5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|Ref.5}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Uptake of biotin. Acts probably by facilitated diffusion. {ECO:0000269|Ref.5}. YigM is a biotin transporter in E. coli K-12 The uptake of labeled biotin is abolished in an E. coli ΔyigM strain (Keio collection strain K-12 BW25113); overexpression of YigM results in increased biotin uptake in both the wild type and in a ΔyigM strain; uptake assays in whole cells and in membrane vesicles suggest biotin is taken up by facilitated diffusion . Biotin transport in E. coli K-12 (strains Y10-1 and 54117-Pasteur collection) is an active process and is inhibited by uncouplers . Biotin transport is regulated by the concentration of biotin in the medium with reduced transport at higher biotin concentrations . Biotinylated peptides up to 31 amino acids long can be taken up by E. coli through the biotin transport system . YigM is predicted to contain 10 transmembrane domains with the C and N-termini located in the cytoplasm . Expression of a yigM promoter reporter decreases with increasing concentration of biotin; a putative truncated BirA binding site is located in the promoter region of YigM . yigM may have a σ54-dependent promoter . Expression of yigM is induced by acivicin . Expression of yigM of E. coli O157:H7 Sakai strain is reduced upon entry into stationary phase .

## Biological Role

Catalyzes TRANS-RXN0-240 (reaction.ecocyc.TRANS-RXN0-240).

## Annotation

FUNCTION: Uptake of biotin. Acts probably by facilitated diffusion. {ECO:0000269|Ref.5}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-240|reaction.ecocyc.TRANS-RXN0-240]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3827|gene.b3827]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADP5`
- `KEGG:ecj:JW3803;eco:b3827;`
- `GeneID:93778110;948309;`
- `GO:GO:0005886; GO:0016020`

## Notes

Biotin transporter (Plasmamembrane biotin transport protein)
