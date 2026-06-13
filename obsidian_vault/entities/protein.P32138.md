---
entity_id: "protein.P32138"
entity_type: "protein"
name: "yihQ"
source_database: "UniProt"
source_id: "P32138"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihQ squQ b3878 JW3849"
---

# yihQ

`protein.P32138`

## Static

- Type: `protein`
- Source: `UniProt:P32138`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of sulfoquinovosyl diacylglycerides (SQDG) to sulfoquinovose (SQ), which is then degraded by E.coli through the SQ Embden-Meyerhof-Parnas (SQ-EMP) sulfoglycolysis pathway as a source of carbon and sulfur. Therefore, is likely involved in the utilization of the sulfoquinovose headgroup found in ubiquitous plant sulfolipids (PubMed:26878550). Is also able to hydrolyze simple sulfoquinovosides such as sulfoquinovosyl glycerol (SQGro) (PubMed:26878550, PubMed:30276262). In vitro, can use the substrate analog para-nitrophenyl alpha-sulfoquinovoside (PNPSQ), but shows no detectable activity toward 4-nitrophenyl alpha-D-glucopyranoside (PNPGlc) (PubMed:26878550, PubMed:30276262). Is a retaining glycoside hydrolase, since it forms the alpha anomer of SQ (PubMed:26878550). Also exhibits some alpha-glucosidase activity against alpha-glucosyl fluoride in vitro, although natural substrates, such as alpha-glucobioses are scarcely hydrolyzed (PubMed:15294295). {ECO:0000269|PubMed:15294295, ECO:0000269|PubMed:26878550, ECO:0000269|PubMed:30276262}. Sulfoquinovosidase (YihQ) catalyzes the hydrolysis of terminal non-reducing sulfoquinovoside residues in sulfoquinovosyl diacylglycerides and sulfoquinovosyl glycerol, releasing the α anomer of sulfoquinovose . Sulfoquinovosyl glycerol can serve as the sole source of carbon and energy via the PWY-7446 pathway...

## Biological Role

Catalyzes RXN-17700 (reaction.ecocyc.RXN-17700), RXN-17701 (reaction.ecocyc.RXN-17701).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of sulfoquinovosyl diacylglycerides (SQDG) to sulfoquinovose (SQ), which is then degraded by E.coli through the SQ Embden-Meyerhof-Parnas (SQ-EMP) sulfoglycolysis pathway as a source of carbon and sulfur. Therefore, is likely involved in the utilization of the sulfoquinovose headgroup found in ubiquitous plant sulfolipids (PubMed:26878550). Is also able to hydrolyze simple sulfoquinovosides such as sulfoquinovosyl glycerol (SQGro) (PubMed:26878550, PubMed:30276262). In vitro, can use the substrate analog para-nitrophenyl alpha-sulfoquinovoside (PNPSQ), but shows no detectable activity toward 4-nitrophenyl alpha-D-glucopyranoside (PNPGlc) (PubMed:26878550, PubMed:30276262). Is a retaining glycoside hydrolase, since it forms the alpha anomer of SQ (PubMed:26878550). Also exhibits some alpha-glucosidase activity against alpha-glucosyl fluoride in vitro, although natural substrates, such as alpha-glucobioses are scarcely hydrolyzed (PubMed:15294295). {ECO:0000269|PubMed:15294295, ECO:0000269|PubMed:26878550, ECO:0000269|PubMed:30276262}.

## Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17700|reaction.ecocyc.RXN-17700]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17701|reaction.ecocyc.RXN-17701]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3878|gene.b3878]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32138`
- `KEGG:ecj:JW3849;eco:b3878;ecoc:C3026_20965;`
- `GeneID:948376;`
- `GO:GO:0004553; GO:0005975; GO:0030246; GO:0061720; GO:1990929`
- `EC:3.2.1.199`

## Notes

Sulfoquinovosidase (SQase) (EC 3.2.1.199)
