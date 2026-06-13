---
entity_id: "protein.P0A7V0"
entity_type: "protein"
name: "rpsB"
source_database: "UniProt"
source_id: "P0A7V0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rpsB b0169 JW0164"
---

# rpsB

`protein.P0A7V0`

## Static

- Type: `protein`
- Source: `UniProt:P0A7V0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Required for ribosomal protein bS1 (rpsA) to bind to the 30S subunit. {ECO:0000269|PubMed:12068815}. The S2 protein, a component of the 30S subunit of the ribosome, is essential in E. coli . S2 is required for S1 binding to the ribosome . Overexpression of csdA, a DEAD-box RNA helicase, supresses the defect of a temperature-sensitive allele of rpsB by restoring assembly of both S1 and S2 with the ribosome at the non-permissive temperature . Expression of S2 is autoregulated, involving conserved elements located in the 5' UTR of the rpsB-tsf mRNA. Regulation may also involve the S1 protein . Purified S2 protein binds to inorganic polyphosphate (polyP). In the presence of polyP, S2 forms a complex with the Lon protease and is degraded by it . S2 was also shown to crosslink to IF3 . A protein-enzyme interactions (PEIs) study that examined the connection between protein-protein interactions (PPIs) and metabolomics networks studied in 22 different environmental conditions found that the PEI RpsB-ADHE-MONOMER AdhE may have a previously unknown role in regulating metabolism, in part because the PEI is conserved across many other bacterial taxa . A low-resolution cryo-electron microscopy map of the ribosome containing S2 has been analyzed .

## Biological Role

Component of 30S ribosomal subunit (complex.ecocyc.CPLX0-3953).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: Required for ribosomal protein bS1 (rpsA) to bind to the 30S subunit. {ECO:0000269|PubMed:12068815}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3953|complex.ecocyc.CPLX0-3953]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b0169|gene.b0169]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7V0`
- `KEGG:ecj:JW0164;eco:b0169;ecoc:C3026_00770;`
- `GeneID:86862679;89519558;947874;`
- `GO:GO:0000028; GO:0002181; GO:0003735; GO:0005737; GO:0008270; GO:0022627`

## Notes

Small ribosomal subunit protein uS2 (30S ribosomal protein S2)
