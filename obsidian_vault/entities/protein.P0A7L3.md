---
entity_id: "protein.P0A7L3"
entity_type: "protein"
name: "rplT"
source_database: "UniProt"
source_id: "P0A7L3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rplT pdzA b1716 JW1706"
---

# rplT

`protein.P0A7L3`

## Static

- Type: `protein`
- Source: `UniProt:P0A7L3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: One of the primary rRNA binding proteins, it binds close to the 5'-end of the 23S rRNA. It is important during the early stages of 50S assembly. {ECO:0000269|PubMed:3298242}. The L20 protein is a component of the 50S subunit of the ribosome and autoregulates its own expression and that of L35 at the posttranscriptional level. The N-terminal domain of L20 is required for ribosome assembly, and the C-terminal domain is required for its regulatory function . L20 binds to the 5' terminal third of 23S rRNA . The C-terminal domain of L20 interacts with both 23S rRNA (H40-41) and the translational regulatory region. Proper folding of the L20 binding sites within RNA is required for interaction with L20, and binding of L20 stabilizes their structure . L20 is required for early assembly of the 4.3c core particle, but is not required for function of the mature 50S ribosomal subunit . L20 can replace L24 for the initiation of assembly of the 50S subunit at permissive temperatures in an L24 mutant . L20 can be crosslinked to L13 and L21 . L20 might be required for maintaining the 50S subunit in the correct conformation for binding of aminoacyl-tRNAs . Decreasing the amount of L20 in the cell leads to a decrease in growth rate and the appearance of an aberrant ribosome peak at 41-43S . Expression of rplT is autoregulated at the posttranscriptional level...

## Biological Role

Component of 50S ribosomal subunit (complex.ecocyc.CPLX0-3962).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

FUNCTION: One of the primary rRNA binding proteins, it binds close to the 5'-end of the 23S rRNA. It is important during the early stages of 50S assembly. {ECO:0000269|PubMed:3298242}.

## Pathways

- `eco03010` Ribosome (KEGG)

## Outgoing Edges (3)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3962|complex.ecocyc.CPLX0-3962]] `EcoCyc` `database` - EcoCyc component coefficient=
- `represses` --> [[gene.b1716|gene.b1716]] `RegulonDB` `S` - regulator=RplT; target=rplT; function=-
- `represses` --> [[gene.b1717|gene.b1717]] `RegulonDB` `S` - regulator=RplT; target=rpmI; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1716|gene.b1716]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A7L3`
- `KEGG:ecj:JW1706;eco:b1716;ecoc:C3026_09820;`
- `GeneID:945152;99705465;99807174;`
- `GO:GO:0000027; GO:0000900; GO:0002181; GO:0003729; GO:0003735; GO:0005737; GO:0005829; GO:0022625; GO:0070180`

## Notes

Large ribosomal subunit protein bL20 (50S ribosomal protein L20)
