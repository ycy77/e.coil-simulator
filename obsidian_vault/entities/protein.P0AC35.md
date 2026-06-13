---
entity_id: "protein.P0AC35"
entity_type: "protein"
name: "ttdB"
source_database: "UniProt"
source_id: "P0AC35"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ttdB ygjB b3062 JW3034"
---

# ttdB

`protein.P0AC35`

## Static

- Type: `protein`
- Source: `UniProt:P0AC35`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

L(+)-tartrate dehydratase subunit beta (L-TTD beta) (EC 4.2.1.32) The ttdB gene encodes the β subunit of L-tartrate dehydratase . Expression may be translationally coupled to TtdA . ttdB shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A ttdB deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses . TtdB: "L-tartrate dehydratase B"

## Biological Role

Catalyzes (R,R)-tartrate hydro-lyase (oxaloacetate-forming) (reaction.R00339). Component of L(+)-tartrate dehydratase (complex.ecocyc.LTARTDEHYDRA-CPLX).

## Enriched Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

L(+)-tartrate dehydratase subunit beta (L-TTD beta) (EC 4.2.1.32)

## Pathways

- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00339|reaction.R00339]] `KEGG` `database` - via EC:4.2.1.32
- `is_component_of` --> [[complex.ecocyc.LTARTDEHYDRA-CPLX|complex.ecocyc.LTARTDEHYDRA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3062|gene.b3062]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AC35`
- `KEGG:ecj:JW3034;eco:b3062;ecoc:C3026_16730;`
- `GeneID:86861212;947568;`
- `GO:GO:0008730; GO:0009408; GO:1901276; GO:1902494`
- `EC:4.2.1.32`

## Notes

L(+)-tartrate dehydratase subunit beta (L-TTD beta) (EC 4.2.1.32)
