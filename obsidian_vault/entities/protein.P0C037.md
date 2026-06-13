---
entity_id: "protein.P0C037"
entity_type: "protein"
name: "ppnP"
source_database: "UniProt"
source_id: "P0C037"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ppnP yaiE b0391 JW0382"
---

# ppnP

`protein.P0C037`

## Static

- Type: `protein`
- Source: `UniProt:P0C037`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the phosphorolysis of diverse nucleosides, yielding D-ribose 1-phosphate and the respective free bases. Can use uridine, adenosine, guanosine, cytidine, thymidine, inosine and xanthosine as substrates. Also catalyzes the reverse reactions. Is not able to produce D-ribose 1-phosphate from D-ribose and phosphate. {ECO:0000269|PubMed:27941785}.

## Biological Role

Catalyzes guanosine:phosphate alpha-D-ribosyltransferase (reaction.R02147), purine-deoxynucleoside:phosphate ribosyltransferase (reaction.R10244). Component of nucleoside phosphorylase PpnP (complex.ecocyc.CPLX0-8619).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Catalyzes the phosphorolysis of diverse nucleosides, yielding D-ribose 1-phosphate and the respective free bases. Can use uridine, adenosine, guanosine, cytidine, thymidine, inosine and xanthosine as substrates. Also catalyzes the reverse reactions. Is not able to produce D-ribose 1-phosphate from D-ribose and phosphate. {ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R02147|reaction.R02147]] `KEGG` `database` - via EC:2.4.2.1
- `catalyzes` --> [[reaction.R10244|reaction.R10244]] `KEGG` `database` - via EC:2.4.2.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8619|complex.ecocyc.CPLX0-8619]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0391|gene.b0391]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C037`
- `KEGG:ecj:JW0382;eco:b0391;ecoc:C3026_01900;`
- `GeneID:86862938;93777070;945048;`
- `GO:GO:0004731; GO:0004850; GO:0005829; GO:0009032; GO:0016154; GO:0042803; GO:0047975`
- `EC:2.4.2.1; 2.4.2.2`

## Notes

Pyrimidine/purine nucleoside phosphorylase (EC 2.4.2.1) (EC 2.4.2.2) (Adenosine phosphorylase) (Cytidine phosphorylase) (Guanosine phosphorylase) (Inosine phosphorylase) (Thymidine phosphorylase) (Uridine phosphorylase) (Xanthosine phosphorylase)
