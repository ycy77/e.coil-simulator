---
entity_id: "protein.P0ABP8"
entity_type: "protein"
name: "deoD"
source_database: "UniProt"
source_id: "P0ABP8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "deoD pup b4384 JW4347"
---

# deoD

`protein.P0ABP8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABP8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible phosphorolytic breakdown of the N-glycosidic bond in the beta-(deoxy)ribonucleoside molecules, with the formation of the corresponding free purine bases and pentose-1-phosphate (PubMed:11786017, PubMed:21672603, PubMed:235429, PubMed:30337572). Acts on 6-amino and 6-oxopurines including deoxyinosine, deoxyguanosine, deoxyadenosine, adenosine, guanosine, and inosine (PubMed:11786017, PubMed:21672603, PubMed:235429, PubMed:30337572). Does not act on xanthosine (Probable). May also catalyze a phosphate-dependent transfer of the pentose moiety from one purine base to another (PubMed:235429). {ECO:0000269|PubMed:11786017, ECO:0000269|PubMed:21672603, ECO:0000269|PubMed:235429, ECO:0000269|PubMed:30337572, ECO:0000305|PubMed:235429}.

## Biological Role

Catalyzes guanosine:phosphate alpha-D-ribosyltransferase (reaction.R02147), purine-deoxynucleoside:phosphate ribosyltransferase (reaction.R10244). Component of purine nucleoside phosphorylase (complex.ecocyc.DEOD-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible phosphorolytic breakdown of the N-glycosidic bond in the beta-(deoxy)ribonucleoside molecules, with the formation of the corresponding free purine bases and pentose-1-phosphate (PubMed:11786017, PubMed:21672603, PubMed:235429, PubMed:30337572). Acts on 6-amino and 6-oxopurines including deoxyinosine, deoxyguanosine, deoxyadenosine, adenosine, guanosine, and inosine (PubMed:11786017, PubMed:21672603, PubMed:235429, PubMed:30337572). Does not act on xanthosine (Probable). May also catalyze a phosphate-dependent transfer of the pentose moiety from one purine base to another (PubMed:235429). {ECO:0000269|PubMed:11786017, ECO:0000269|PubMed:21672603, ECO:0000269|PubMed:235429, ECO:0000269|PubMed:30337572, ECO:0000305|PubMed:235429}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02147|reaction.R02147]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` --> [[reaction.R10244|reaction.R10244]] `KEGG` `database` - via EC:2.4.2.1
- `is_component_of` --> [[complex.ecocyc.DEOD-CPLX|complex.ecocyc.DEOD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b4384|gene.b4384]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABP8`
- `KEGG:ecj:JW4347;eco:b4384;ecoc:C3026_23690;`
- `GeneID:93777460;945654;`
- `GO:GO:0004731; GO:0005829; GO:0006152; GO:0006974; GO:0016020; GO:0019686; GO:0042802; GO:0047975`
- `EC:2.4.2.1`

## Notes

Purine nucleoside phosphorylase DeoD-type (PNP) (EC 2.4.2.1)
