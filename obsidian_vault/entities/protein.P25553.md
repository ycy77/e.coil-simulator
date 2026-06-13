---
entity_id: "protein.P25553"
entity_type: "protein"
name: "aldA"
source_database: "UniProt"
source_id: "P25553"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aldA ald b1415 JW1412"
---

# aldA

`protein.P25553`

## Static

- Type: `protein`
- Source: `UniProt:P25553`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the irreversible oxidation of L-lactaldehyde to L-lactate (PubMed:27671251, PubMed:3298215, PubMed:3308886, PubMed:6345530). Also shows high activity with glycolaldehyde and L-glyceraldehyde (PubMed:16731973, PubMed:31850327, PubMed:3275622, PubMed:3308886, PubMed:6345530). Has weaker activity with various aldehydes such as methylglyoxal, propionaldehyde or benzaldehyde (PubMed:16731973, PubMed:3308886). Involved in the degradation of lactaldehyde produced during metabolism of L-fucose and L-rhamnose (PubMed:3275622, PubMed:3298215). It may be involved in several other metabolic pathways (PubMed:3308886). {ECO:0000269|PubMed:16731973, ECO:0000269|PubMed:27671251, ECO:0000269|PubMed:31850327, ECO:0000269|PubMed:3275622, ECO:0000269|PubMed:3298215, ECO:0000269|PubMed:3308886, ECO:0000269|PubMed:6345530}. Aldehyde dehydrogenase A (AldA) is an NAD+-dependent dehydrogenase of relatively broad specificity for small α-hydroxyaldehyde substrates. It is thus utilized in several metabolic pathways . The glycolaldehyde dehydrogenase activity of AldA may serve an essential function in removing the glycolaldehyde side product of H2NEOPTERINALDOL-MONOMER FolB within the folate biosynthesis pathway. The function can be bypassed by G6198-MONOMER PrpC...

## Biological Role

Catalyzes pyruvaldehyde:NAD+ oxidoreductase; (reaction.R00203). Component of aldehyde dehydrogenase A, NAD-linked (complex.ecocyc.ALD-CPLX).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the irreversible oxidation of L-lactaldehyde to L-lactate (PubMed:27671251, PubMed:3298215, PubMed:3308886, PubMed:6345530). Also shows high activity with glycolaldehyde and L-glyceraldehyde (PubMed:16731973, PubMed:31850327, PubMed:3275622, PubMed:3308886, PubMed:6345530). Has weaker activity with various aldehydes such as methylglyoxal, propionaldehyde or benzaldehyde (PubMed:16731973, PubMed:3308886). Involved in the degradation of lactaldehyde produced during metabolism of L-fucose and L-rhamnose (PubMed:3275622, PubMed:3298215). It may be involved in several other metabolic pathways (PubMed:3308886). {ECO:0000269|PubMed:16731973, ECO:0000269|PubMed:27671251, ECO:0000269|PubMed:31850327, ECO:0000269|PubMed:3275622, ECO:0000269|PubMed:3298215, ECO:0000269|PubMed:3308886, ECO:0000269|PubMed:6345530}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00203|reaction.R00203]] `KEGG` `database` - via EC:1.2.1.22
- `is_component_of` --> [[complex.ecocyc.ALD-CPLX|complex.ecocyc.ALD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1415|gene.b1415]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25553`
- `KEGG:ecj:JW1412;eco:b1415;ecoc:C3026_08240;`
- `GeneID:945672;`
- `GO:GO:0004777; GO:0005829; GO:0008911; GO:0009450; GO:0019301; GO:0032991; GO:0042355; GO:0042802; GO:0050569`
- `EC:1.2.1.21; 1.2.1.22`

## Notes

Lactaldehyde dehydrogenase (EC 1.2.1.22) (Aldehyde dehydrogenase A) (Glycolaldehyde dehydrogenase) (EC 1.2.1.21)
