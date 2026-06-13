---
entity_id: "protein.P60716"
entity_type: "protein"
name: "lipA"
source_database: "UniProt"
source_id: "P60716"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00206}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lipA lip b0628 JW0623"
---

# lipA

`protein.P60716`

## Static

- Type: `protein`
- Source: `UniProt:P60716`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00206}.

## Enriched Summary

FUNCTION: Catalyzes the radical-mediated insertion of two sulfur atoms into the C-6 and C-8 positions of the octanoyl moiety bound to the lipoyl domains of lipoate-dependent enzymes, thereby converting the octanoylated domains into lipoylated derivatives. Free octanoate is not a substrate for LipA. {ECO:0000269|PubMed:11106496, ECO:0000269|PubMed:14700636, ECO:0000269|PubMed:15157071}. Lipoate synthase catalyzes the final step of de novo lipoate biosynthesis, the insertion of sulfur into the octanoyl side chain of an octanoylated E2 domain to form the lipoate moiety . Lipoate modification of the E2 subunits is important for the function of PYRUVATEDEH-CPLX , 2OXOGLUTARATEDEH-CPLX "α-ketoglutarate dehydrogenase" , and the GCVMULTI-CPLX . Lipoate synthase is a homodimer containing iron-sulfur clusters . Coexpression with the isc operon increases the yield of overexpressed soluble LipA . LipA belongs to the radical SAM superfamily of enzymes . The enzyme uses octanoyl side chains (but not free octanoate) as substrate . The 5'-dA· radicals, generated from SAM, act directly on the octanoyl substrate. Two equivalents of 5'-dA· sequentially abstract hydrogen atoms from C6 and C8 of the octanoyl group, preparing it for sulfur insertion...

## Biological Role

Catalyzes [protein]-N6-(octanoyl)-L-lysine:an [Fe-S] cluster scaffold protein carrying a [4Fe-4S]2+ cluster sulfurtransferase (reaction.R07767). Component of lipoyl synthase (complex.ecocyc.CPLX0-782).

## Enriched Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the radical-mediated insertion of two sulfur atoms into the C-6 and C-8 positions of the octanoyl moiety bound to the lipoyl domains of lipoate-dependent enzymes, thereby converting the octanoylated domains into lipoylated derivatives. Free octanoate is not a substrate for LipA. {ECO:0000269|PubMed:11106496, ECO:0000269|PubMed:14700636, ECO:0000269|PubMed:15157071}.

## Pathways

- `eco00785` Lipoic acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R07767|reaction.R07767]] `KEGG` `database` - via EC:2.8.1.8
- `is_component_of` --> [[complex.ecocyc.CPLX0-782|complex.ecocyc.CPLX0-782]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0628|gene.b0628]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60716`
- `KEGG:ecj:JW0623;eco:b0628;ecoc:C3026_03135;`
- `GeneID:93776854;945227;`
- `GO:GO:0005737; GO:0005829; GO:0009107; GO:0009249; GO:0016992; GO:0042803; GO:0046872; GO:0051539`
- `EC:2.8.1.8`

## Notes

Lipoyl synthase (EC 2.8.1.8) (Lip-syn) (LS) (Lipoate synthase) (Lipoic acid synthase) (Sulfur insertion protein LipA)
