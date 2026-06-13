---
entity_id: "protein.P0AEG1"
entity_type: "protein"
name: "dppC"
source_database: "UniProt"
source_id: "P0AEG1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dppC b3542 JW3511"
---

# dppC

`protein.P0AEG1`

## Static

- Type: `protein`
- Source: `UniProt:P0AEG1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}. dppB encodes the predicted inner membrane subunit of a dipeptide ABC transport system .

## Biological Role

Component of dipeptide ABC transporter (complex.ecocyc.ABC-8-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter DppABCDF involved in dipeptide transport (PubMed:7536291). Responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:7536291, ECO:0000305}.; FUNCTION: When a foreign outer membrane heme receptor is expressed in E.coli, DppABCDF can also transport heme and its precursor, 5-aminolevulinic acid (ALA), from the periplasm into the cytoplasm. {ECO:0000269|PubMed:16905647, ECO:0000269|PubMed:8444807}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-8-CPLX|complex.ecocyc.ABC-8-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3542|gene.b3542]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEG1`
- `KEGG:ecj:JW3511;eco:b3542;ecoc:C3026_19195;`
- `GeneID:75173735;75201991;948064;`
- `GO:GO:0005886; GO:0015031; GO:0016020; GO:0035351; GO:0042938; GO:0055052; GO:0071916`

## Notes

Dipeptide transport system permease protein DppC
