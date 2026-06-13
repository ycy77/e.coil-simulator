---
entity_id: "protein.P0CI31"
entity_type: "protein"
name: "hcaB"
source_database: "UniProt"
source_id: "P0CI31"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcaB phdD yfhX b2541 JW2525"
---

# hcaB

`protein.P0CI31`

## Static

- Type: `protein`
- Source: `UniProt:P0CI31`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol) into 3-(2,3-dihydroxylphenyl)propanoic acid (DHPP) and 2,3-dihydroxicinnamic acid (DHCI), respectively. {ECO:0000250, ECO:0000269|PubMed:9603882}. Based on sequence similarity, HcaB is thought to encode 2,3-dihydroxy-2,3-dihydrophenylpropionate dehydrogenase . The HcaB enzyme has not been biochemically characterized. E. coli is able to utilize certain aromatic acids as carbon and energy sources. A meta-cleavage pathway involving HcaB is used for the catabolism of 3-phenylpropionate . An hcaB mutant does not grow on m-hydroxyphenylpropionate (MHP) as the sole source of carbon . HcaB: "hydroxycinnamic acid"

## Biological Role

Catalyzes PHENPRODIOLDEHYDROG-RXN (reaction.ecocyc.PHENPRODIOLDEHYDROG-RXN), RXN-12071 (reaction.ecocyc.RXN-12071).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

FUNCTION: Converts 3-phenylpropionate-dihydrodiol (PP-dihydrodiol) and cinnamic acid-dihydrodiol (CI-dihydrodiol) into 3-(2,3-dihydroxylphenyl)propanoic acid (DHPP) and 2,3-dihydroxicinnamic acid (DHCI), respectively. {ECO:0000250, ECO:0000269|PubMed:9603882}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PHENPRODIOLDEHYDROG-RXN|reaction.ecocyc.PHENPRODIOLDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-12071|reaction.ecocyc.RXN-12071]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2541|gene.b2541]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0CI31`
- `KEGG:ecj:JW2525;eco:b2541;ecoc:C3026_14075;`
- `GeneID:945346;`
- `GO:GO:0018498; GO:0019380`
- `EC:1.3.1.87`

## Notes

3-phenylpropionate-dihydrodiol/cinnamic acid-dihydrodiol dehydrogenase (EC 1.3.1.87) (2,3-dihydroxy-2,3-dihydrophenylpropionate dehydrogenase) (3-(cis-5,6-dihydroxycyclohexa-1,3-dien-1-yl)propanoate dehydrogenase) (CI-dihydrodiol dehydrogenase) (Cis-3-(2-carboxyethenyl)-3,5-cyclohexadiene-1,2-diol dehydrogenase) (Cis-3-(2-carboxyethyl)-3,5-cyclohexadiene-1,2-diol dehydrogenase) (PP-dihydrodiol dehydrogenase)
