---
entity_id: "protein.P03023"
entity_type: "protein"
name: "lacI"
source_database: "UniProt"
source_id: "P03023"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lacI b0345 JW0336"
---

# lacI

`protein.P03023`

## Static

- Type: `protein`
- Source: `UniProt:P03023`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Repressor of the lactose operon. Binds allolactose as an inducer. The Lactose inhibitor," LacI, is a DNA-binding transcription factor that represses transcription of the operon involved in transport and catabolism of lactose . In the absence of allolactose, LacI represses the lac operon by preventing open promoter complex formation for transcription . In this repression system, LacI binds to three operators, and formation of a repressor loop between two of them is critical . This repressor binds in tandem to inverted repeat sequences that are 21 nucleotides long and possess conserved motifs . LacI is negatively autoregulated when it binds to two DNA-binding sites, one located downstream of the lacI gene and the other one located in the coding sequence for the C terminus of LacI. The protein when bound to these sites forms a loop that inhibits the transcription elongation, thus producing truncated proteins that are tagged for degradation by the small peptide SsrA . More generally, LacI repression by blocking open complex formation is compatible with RNAP-promoter stabilization at earlier steps; in vivo, LacI follows the reciprocal scaling of fold-change with promoter basal activity, buffering promoter-to-promoter variability across contexts...

## Biological Role

Component of LacI-allolactose (complex.ecocyc.MONOMER0-159).

## Annotation

FUNCTION: Repressor of the lactose operon. Binds allolactose as an inducer.

## Outgoing Edges (4)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-159|complex.ecocyc.MONOMER0-159]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b0342|gene.b0342]] `RegulonDB` `C` - regulator=LacI; target=lacA; function=-
- `represses` --> [[gene.b0343|gene.b0343]] `RegulonDB` `C` - regulator=LacI; target=lacY; function=-
- `represses` --> [[gene.b0344|gene.b0344]] `RegulonDB` `C` - regulator=LacI; target=lacZ; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0345|gene.b0345]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03023`
- `KEGG:ecj:JW0336;eco:b0345;ecoc:C3026_04265;ecoc:C3026_04585;ecoc:C3026_04905;ecoc:C3026_24860;`
- `GeneID:945007;`
- `GO:GO:0000976; GO:0000987; GO:0001217; GO:0003700; GO:0005829; GO:0006355; GO:0042802; GO:0045892`

## Notes

Lactose operon repressor
