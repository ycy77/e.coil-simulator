---
entity_id: "protein.P45563"
entity_type: "protein"
name: "xapA"
source_database: "UniProt"
source_id: "P45563"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "xapA pndA b2407 JW2398"
---

# xapA

`protein.P45563`

## Static

- Type: `protein`
- Source: `UniProt:P45563`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: The purine nucleoside phosphorylases catalyze the phosphorolytic breakdown of the N-glycosidic bond in the beta-(deoxy)ribonucleoside molecules, with the formation of the corresponding free purine bases and pentose-1-phosphate. This protein can degrade all purine nucleosides including xanthosine, inosine and guanosine, but cannot cleave adenosine, deoxyadenosine or hypoxanthine arabinoside. Has a preference for the neutral over the monoanionic form of xanthosine. {ECO:0000269|PubMed:15808857, ECO:0000269|PubMed:3042752, ECO:0000269|PubMed:7007808, ECO:0000269|PubMed:7007809}.

## Biological Role

Catalyzes guanosine:phosphate alpha-D-ribosyltransferase (reaction.R02147), purine-deoxynucleoside:phosphate ribosyltransferase (reaction.R10244). Component of xanthosine phosphorylase (complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: The purine nucleoside phosphorylases catalyze the phosphorolytic breakdown of the N-glycosidic bond in the beta-(deoxy)ribonucleoside molecules, with the formation of the corresponding free purine bases and pentose-1-phosphate. This protein can degrade all purine nucleosides including xanthosine, inosine and guanosine, but cannot cleave adenosine, deoxyadenosine or hypoxanthine arabinoside. Has a preference for the neutral over the monoanionic form of xanthosine. {ECO:0000269|PubMed:15808857, ECO:0000269|PubMed:3042752, ECO:0000269|PubMed:7007808, ECO:0000269|PubMed:7007809}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02147|reaction.R02147]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` --> [[reaction.R10244|reaction.R10244]] `KEGG` `database` - via EC:2.4.2.1
- `is_component_of` --> [[complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX|complex.ecocyc.XANTHOSINEPHOSPHORY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2407|gene.b2407]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45563`
- `KEGG:ecj:JW2398;eco:b2407;ecoc:C3026_13380;`
- `GeneID:946878;`
- `GO:GO:0004731; GO:0005737; GO:0006148; GO:0006149; GO:0006152; GO:0006161; GO:0015949; GO:0034214; GO:0034355; GO:0042802; GO:0046115; GO:0047724; GO:0047975; GO:0055086; GO:1903228`
- `EC:2.4.2.1`

## Notes

Purine nucleoside phosphorylase 2 (EC 2.4.2.1) (Inosine-guanosine phosphorylase) (Purine nucleoside phosphorylase II) (PNP II) (Xanthosine phosphorylase)
