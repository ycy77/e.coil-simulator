---
entity_id: "protein.P75989"
entity_type: "protein"
name: "bluR"
source_database: "UniProt"
source_id: "P75989"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bluR ycgE b1162 JW1149"
---

# bluR

`protein.P75989`

## Static

- Type: `protein`
- Source: `UniProt:P75989`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Controls the expression of several small proteins that may play a role in biofilm maturation. Binds to and represses the operator of the ycgZ-ymgA-ariR-ymgC operon and also regulates ynaK. Binding is antagonized by BluF upon blue light (470 nm) irradiation. Blue light may increase the affinity of BluF for BluR, allowing it to be released from its operator. {ECO:0000269|PubMed:19240136, ECO:0000269|PubMed:22783906}. BluR is a MerR-like regulator that contains an N-terminal helix-turn-helix DNA-binding region and a ligand-binding region in the C-terminal domain . BluR functions as a repressor for genes involved in the modulation of biofilm formation and for acid resistance genes . Its expression is strongly induced at low temperatures . BluR is a paralogue of MlrA, and it represses the transcription of the ycgZ-ymgA-ariR-ymgC operon . This operon is transcribed divergently on the opposite strand, under the control of σ38 (RpoS) RNA polymerase . Its gene products are involved in the production of colanic acid, a component of the biofilm matrix, via the Rcs phosphorelay system . The bluRF-ycgZ-ymgA-ariR region is conserved in various enteric bacteria . BluR binds to the promoter region of ycgZ. BluF is an antagonist of BluR . It binds to the N-terminal domain of BluR and inhibits the DNA-binding activity of BluR. Binding of BluF to BluR is stimulated by blue light...

## Annotation

FUNCTION: Controls the expression of several small proteins that may play a role in biofilm maturation. Binds to and represses the operator of the ycgZ-ymgA-ariR-ymgC operon and also regulates ynaK. Binding is antagonized by BluF upon blue light (470 nm) irradiation. Blue light may increase the affinity of BluF for BluR, allowing it to be released from its operator. {ECO:0000269|PubMed:19240136, ECO:0000269|PubMed:22783906}.

## Outgoing Edges (4)

- `represses` --> [[gene.b1164|gene.b1164]] `RegulonDB` `C` - regulator=BluR; target=ycgZ; function=-
- `represses` --> [[gene.b1165|gene.b1165]] `RegulonDB` `C` - regulator=BluR; target=ymgA; function=-
- `represses` --> [[gene.b1166|gene.b1166]] `RegulonDB` `C` - regulator=BluR; target=ariR; function=-
- `represses` --> [[gene.b1167|gene.b1167]] `RegulonDB` `C` - regulator=BluR; target=ymgC; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1162|gene.b1162]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75989`
- `KEGG:ecj:JW1149;eco:b1162;ecoc:C3026_06850;`
- `GeneID:75203725;945735;`
- `GO:GO:0003677; GO:0003700; GO:0006355; GO:0045892`

## Notes

HTH-type transcriptional repressor BluR
