---
entity_id: "protein.P32131"
entity_type: "protein"
name: "hemN"
source_database: "UniProt"
source_id: "P32131"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12114526}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hemN yihJ b3867 JW3838"
---

# hemN

`protein.P32131`

## Static

- Type: `protein`
- Source: `UniProt:P32131`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:12114526}.

## Enriched Summary

FUNCTION: Involved in the heme biosynthesis. Catalyzes the anaerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen III to yield the vinyl groups in protoporphyrinogen IX. It can use NAD or NADP, but NAD is preferred. {ECO:0000269|PubMed:12114526, ECO:0000269|PubMed:7768836}. Oxidative decarboxylation of coproporphyrinogen III to protoporphyrinogen IX is catalyzed by two enzymes in E. coli. Under aerobic conditions, the EG12189 hemF gene product is active. Under anaerobic conditions, HemN catalyzes the coproporphyrinogen III dehydrogenase reaction . HemN is monomeric when overproduced and purified under anaerobic conditions and might be membrane-associated in vivo. The enzyme contains an oxygen-sensitive [4Fe-4S] iron-sulfur cluster; mutations in specific residues important for iron-sulfur cluster coordination and catalysis have been analyzed and a catalytic mechanism has been proposed . HemN has been classified as a "Radical SAM" enzyme . S-adenosylmethionine (SAM) is consumed during catalysis; the role of a second SAM binding site in HemN has been investigated by site-directed mutagenesis . The catalytic mechanism has been studied in detail . Recently, proposed a revised catalytic mechanism elucidating the function of the second SAM molecule present in the active site. A crystal structure of HemN has been solved at 2.07 Å resolution...

## Biological Role

Catalyzes coproporphyrinogen-III:S-adenosyl-L-methionine oxidoreductase(decarboxylating) (reaction.R06895), HEMN-RXN (reaction.ecocyc.HEMN-RXN). Bound by a [4Fe-4S] iron-sulfur cluster (molecule.ecocyc.CPD-7).

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Involved in the heme biosynthesis. Catalyzes the anaerobic oxidative decarboxylation of propionate groups of rings A and B of coproporphyrinogen III to yield the vinyl groups in protoporphyrinogen IX. It can use NAD or NADP, but NAD is preferred. {ECO:0000269|PubMed:12114526, ECO:0000269|PubMed:7768836}.

## Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R06895|reaction.R06895]] `KEGG` `database` - via EC:1.3.98.3
- `catalyzes` --> [[reaction.ecocyc.HEMN-RXN|reaction.ecocyc.HEMN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.CPD-7|molecule.ecocyc.CPD-7]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b3867|gene.b3867]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32131`
- `KEGG:ecj:JW3838;eco:b3867;ecoc:C3026_20900;`
- `GeneID:93778070;948362;`
- `GO:GO:0004109; GO:0005737; GO:0006782; GO:0019353; GO:0046872; GO:0051539; GO:0051989`
- `EC:1.3.98.3`

## Notes

Oxygen-independent coproporphyrinogen III oxidase (CPO) (EC 1.3.98.3) (Coproporphyrinogen III dehydrogenase) (CPDH)
