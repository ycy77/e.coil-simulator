---
entity_id: "protein.P0A9S5"
entity_type: "protein"
name: "gldA"
source_database: "UniProt"
source_id: "P0A9S5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gldA b3945 JW5556"
---

# gldA

`protein.P0A9S5`

## Static

- Type: `protein`
- Source: `UniProt:P0A9S5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NAD-dependent oxidation of glycerol to dihydroxyacetone (glycerone) (PubMed:18179582, PubMed:3920199, PubMed:40950, PubMed:6365902, PubMed:8132480). Allows microorganisms to utilize glycerol as a source of carbon under anaerobic conditions (PubMed:18632294). In E.coli, an important role of GldA is also likely to regulate the intracellular level of dihydroxyacetone by catalyzing the reverse reaction, i.e. the conversion of dihydroxyacetone into glycerol (PubMed:18179582). Possesses a broad substrate specificity, since it is also able to oxidize 1,2-propanediol and several of its analogs, DL-2,3-butanediol and D-1-amino-2-propanol, and to reduce dihydroxyacetone, hydroxyacetone, glycolaldehyde and methylglyoxal into glycerol, 1,2-propanediol, ethylene glycol and lactaldehyde, respectively (PubMed:18179582, PubMed:3920199, PubMed:40950, PubMed:4385233, PubMed:6365902). {ECO:0000269|PubMed:18179582, ECO:0000269|PubMed:18632294, ECO:0000269|PubMed:3920199, ECO:0000269|PubMed:40950, ECO:0000269|PubMed:4385233, ECO:0000269|PubMed:6365902, ECO:0000269|PubMed:8132480}.

## Biological Role

Component of L-1,2-propanediol dehydrogenase / glycerol dehydrogenase (complex.ecocyc.GLYCDEH-CPLX).

## Enriched Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD-dependent oxidation of glycerol to dihydroxyacetone (glycerone) (PubMed:18179582, PubMed:3920199, PubMed:40950, PubMed:6365902, PubMed:8132480). Allows microorganisms to utilize glycerol as a source of carbon under anaerobic conditions (PubMed:18632294). In E.coli, an important role of GldA is also likely to regulate the intracellular level of dihydroxyacetone by catalyzing the reverse reaction, i.e. the conversion of dihydroxyacetone into glycerol (PubMed:18179582). Possesses a broad substrate specificity, since it is also able to oxidize 1,2-propanediol and several of its analogs, DL-2,3-butanediol and D-1-amino-2-propanol, and to reduce dihydroxyacetone, hydroxyacetone, glycolaldehyde and methylglyoxal into glycerol, 1,2-propanediol, ethylene glycol and lactaldehyde, respectively (PubMed:18179582, PubMed:3920199, PubMed:40950, PubMed:4385233, PubMed:6365902). {ECO:0000269|PubMed:18179582, ECO:0000269|PubMed:18632294, ECO:0000269|PubMed:3920199, ECO:0000269|PubMed:40950, ECO:0000269|PubMed:4385233, ECO:0000269|PubMed:6365902, ECO:0000269|PubMed:8132480}.

## Pathways

- `eco00561` Glycerolipid metabolism (KEGG)
- `eco00640` Propanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.GLYCDEH-CPLX|complex.ecocyc.GLYCDEH-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=8 | EcoCyc protcplxs.col coefficient=8

## Incoming Edges (1)

- `encodes` <-- [[gene.b3945|gene.b3945]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9S5`
- `KEGG:ecj:JW5556;eco:b3945;ecoc:C3026_21325;`
- `GeneID:75203224;948440;`
- `GO:GO:0005829; GO:0008270; GO:0008888; GO:0019147; GO:0019588; GO:0032991; GO:0042802; GO:0051289; GO:0051596`
- `EC:1.1.1.6; 1.1.1.75`

## Notes

Glycerol dehydrogenase (GDH) (GLDH) (EC 1.1.1.6) ((R)-aminopropanol dehydrogenase) (EC 1.1.1.75) (1,2-propanediol dehydrogenase) (D-1-amino-2-propanol oxidoreductase)
