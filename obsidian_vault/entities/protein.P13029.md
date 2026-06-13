---
entity_id: "protein.P13029"
entity_type: "protein"
name: "katG"
source_database: "UniProt"
source_id: "P13029"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "katG b3942 JW3914"
---

# katG

`protein.P13029`

## Static

- Type: `protein`
- Source: `UniProt:P13029`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Bifunctional enzyme with both catalase and broad-spectrum peroxidase activity. Also displays NADH oxidase, INH lyase and isonicotinoyl-NAD synthase activities. {ECO:0000269|PubMed:18178143, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:374409}. There are two distinct catalases in E. coli. The KatG enzyme is the bifunctional hydroperoxidase I (HPI), with both catalase and peroxidase activity. A monofunctional catalase, HPII, is encoded by katE . Endogenously produced H2O2 is primarily scavenged by a third enzyme, CPLX0-245, while catalase is the primary scavenger at high H2O2 concentrations . The catalase activity uses one molecule of H2O2 as the electron donor and a second molecule of H2O2 as the electron acceptor, producing oxygen and water. At lower concentrations of H2O2, the peroxidase activity is able to utilize a suitable electron donor other than H2O2 . For both activities, the initial step is the reduction of H2O2 to H2O by a ferric heme, producing the ferryl porphyrin cation radical intermediate known as compound I. In the catalase reaction, compound I is returned directly to the ferric state by oxidizing a second molecule of H2O2 to O2. Under certain conditions, KatG associates with thioredoxin, which hypothetically could act as the external electron donor...

## Biological Role

Catalyzes hydrogen-peroxide:hydrogen-peroxide oxidoreductase (reaction.R00009), methanol:hydrogen-peroxide oxidoreductase (reaction.R00602), L-phenylalanine:oxygen oxidoreductase (decarboxylating) (reaction.R00698), donor:hydrogen-peroxide oxidoreductase (reaction.R02596), isoniazid:hydrogen-peroxide oxidoreductase (reaction.R11906). Component of catalase/hydroperoxidase HPI (complex.ecocyc.HYDROPEROXIDI-CPLX).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Bifunctional enzyme with both catalase and broad-spectrum peroxidase activity. Also displays NADH oxidase, INH lyase and isonicotinoyl-NAD synthase activities. {ECO:0000269|PubMed:18178143, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:374409}.

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00380` Tryptophan metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (6)

- `catalyzes` --> [[reaction.R00009|reaction.R00009]] `KEGG` `database` - via EC:1.11.1.21
- `catalyzes` --> [[reaction.R00602|reaction.R00602]] `KEGG` `database` - via EC:1.11.1.21
- `catalyzes` --> [[reaction.R00698|reaction.R00698]] `KEGG` `database` - via EC:1.11.1.21
- `catalyzes` --> [[reaction.R02596|reaction.R02596]] `KEGG` `database` - via EC:1.11.1.21
- `catalyzes` --> [[reaction.R11906|reaction.R11906]] `KEGG` `database` - via EC:1.11.1.21
- `is_component_of` --> [[complex.ecocyc.HYDROPEROXIDI-CPLX|complex.ecocyc.HYDROPEROXIDI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3942|gene.b3942]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13029`
- `KEGG:ecj:JW3914;eco:b3942;ecoc:C3026_21305;`
- `GeneID:948431;`
- `GO:GO:0004096; GO:0004601; GO:0005829; GO:0006979; GO:0016491; GO:0020037; GO:0042744; GO:0042802; GO:0046872; GO:0070301`
- `EC:1.11.1.21`

## Notes

Catalase-peroxidase (CP) (EC 1.11.1.21) (Hydroperoxidase I) (HPI) (Peroxidase/catalase)
