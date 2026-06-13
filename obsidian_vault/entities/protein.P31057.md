---
entity_id: "protein.P31057"
entity_type: "protein"
name: "panB"
source_database: "UniProt"
source_id: "P31057"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "panB b0134 JW0130"
---

# panB

`protein.P31057`

## Static

- Type: `protein`
- Source: `UniProt:P31057`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the reversible reaction in which hydroxymethyl group from 5,10-methylenetetrahydrofolate is transferred onto alpha-ketoisovalerate to form ketopantoate. {ECO:0000269|PubMed:6463, ECO:0000269|PubMed:776976}. 3-methyl-2-oxobutanoate hydroxymethyltransferase (KPHMT, PanB) catalyzes the first committed step of the pantothenate biosynthesis pathway, transferring the C11 carbon of 5,10-methylene-tetrahydrofolate onto 2-keto-isovalerate to form 2-dehydropantoate . 2-Dehydropantoate is an essential precursor of pantothenate . A crystal structure of the enzyme in complex with ketopantoate has been solved at 1.9Å resolution. The enzyme is a member of the (βα)8-barrel superfamily of enzymes; the quarternary structure can best be described as a pentamer of dimers . Comparative genomics has suggested a functional association between PanB and H2PTERIDINEPYROPHOSPHOKIN-MONOMER FolK. The proposed hypothesis is that a side reaction catalyzed by PanB damages 5,10-methylenetetrahydrofolate (CH2-THF), and FolK subsequently recycles the resulting pterin moiety to folate. In support of this hypothesis, overexpression of panB increases the cells' sensitivity to antifolate drugs sulfathiazole and trimethoprim. However, overexpression of panB increases the intracellular folate pool...

## Biological Role

Component of 3-methyl-2-oxobutanoate hydroxymethyltransferase (complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible reaction in which hydroxymethyl group from 5,10-methylenetetrahydrofolate is transferred onto alpha-ketoisovalerate to form ketopantoate. {ECO:0000269|PubMed:6463, ECO:0000269|PubMed:776976}.

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX|complex.ecocyc.3-METHYL-2-OXOBUT-OHCH3XFER-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=10 | EcoCyc protcplxs.col coefficient=10

## Incoming Edges (1)

- `encodes` <-- [[gene.b0134|gene.b0134]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31057`
- `KEGG:ecj:JW0130;eco:b0134;ecoc:C3026_00575;`
- `GeneID:944839;`
- `GO:GO:0000287; GO:0003864; GO:0005737; GO:0005829; GO:0015940; GO:0016020; GO:0042802`
- `EC:2.1.2.11`

## Notes

3-methyl-2-oxobutanoate hydroxymethyltransferase (EC 2.1.2.11) (Ketopantoate hydroxymethyltransferase) (KPHMT)
