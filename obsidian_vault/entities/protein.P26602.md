---
entity_id: "protein.P26602"
entity_type: "protein"
name: "ubiC"
source_database: "UniProt"
source_id: "P26602"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ubiC b4039 JW5713"
---

# ubiC

`protein.P26602`

## Static

- Type: `protein`
- Source: `UniProt:P26602`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Removes the pyruvyl group from chorismate, with concomitant aromatization of the ring, to provide 4-hydroxybenzoate (4HB) for the ubiquinone pathway. {ECO:0000269|PubMed:11825618, ECO:0000269|PubMed:16343413, ECO:0000269|PubMed:1644758, ECO:0000269|PubMed:8012607}. Chorismate pyruvate—lyase (CPL) catalyzes the first committed step in the biosynthesis of ubiquinone, the conversion of chorismate to 4-hydroxybenzoate . The enzyme retains and is efficiently inhibited by the 4-hydroxybenzoate reaction product, which may present a control mechanism for the ubiquinone biosynthesis pathway or a mechanism for delivery of 4-hydroxybenzoate to the membrane . Crystal structures of the enzyme in various forms have been solved; the structures have revealed the basis for tight product binding and the structural basis for the catalytic and product release mechanisms . A ubiC mutant can grow on glucose as the sole source of carbon, but can not grow on malate or succinate unless 4-hydroxybenzoate is provided . The growth yield of a ubiCA mutant grown aerobically on glucose or glycerol is much lower than that of wild-type . Overexpression of ubiC can complement a pabC mutation, although the purified protein did not have appreciable activity with 4-amino-4-deoxychorismate as the substrate...

## Biological Role

Catalyzes CHORPYRLY-RXN (reaction.ecocyc.CHORPYRLY-RXN).

## Enriched Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Removes the pyruvyl group from chorismate, with concomitant aromatization of the ring, to provide 4-hydroxybenzoate (4HB) for the ubiquinone pathway. {ECO:0000269|PubMed:11825618, ECO:0000269|PubMed:16343413, ECO:0000269|PubMed:1644758, ECO:0000269|PubMed:8012607}.

## Pathways

- `eco00130` Ubiquinone and other terpenoid-quinone biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.CHORPYRLY-RXN|reaction.ecocyc.CHORPYRLY-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4039|gene.b4039]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P26602`
- `KEGG:ecj:JW5713;eco:b4039;ecoc:C3026_21830;`
- `GeneID:948545;`
- `GO:GO:0005829; GO:0006744; GO:0008813; GO:0042866`
- `EC:4.1.3.40`

## Notes

Chorismate pyruvate-lyase (CL) (CPL) (EC 4.1.3.40)
