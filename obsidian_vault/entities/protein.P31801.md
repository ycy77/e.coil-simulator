---
entity_id: "protein.P31801"
entity_type: "protein"
name: "chaA"
source_database: "UniProt"
source_id: "P31801"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chaA b1216 JW1207"
---

# chaA

`protein.P31801`

## Static

- Type: `protein`
- Source: `UniProt:P31801`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Sodium exporter that functions mainly at alkaline pH (PubMed:8021217, PubMed:8496184, PubMed:9518629). Can also function as a potassium/proton and calcium/proton antiporter at alkaline pH (PubMed:16687400, PubMed:18342619, PubMed:8021217, PubMed:8496184). Does not play a major role in calcium export (PubMed:18342619). The K(+)/H(+) antiporter activity may enable E.coli to adapt to K(+) salinity stress and to maintain K(+) homeostasis (PubMed:16687400). {ECO:0000269|PubMed:16687400, ECO:0000269|PubMed:18342619, ECO:0000269|PubMed:8021217, ECO:0000269|PubMed:8496184, ECO:0000269|PubMed:9518629}. ChaA is an Na+/K+:proton antiporter which contributes to growth at alkaline pH.E. coli appears to contain a number of transporters which mediate active proton uptake for alkaline pH homeostasis including CPLX0-7629 "NhaA" (the prominent Na+:H+ antiporter), NHAB-MONOMER "NhaB", CMR-MONOMER "MdfA" and YJIO-MONOMER "MdtM", each of which may function under varying conditions of external pH and cation composition (see ) Overexpression of chaA complements the Na+ sensitivity of E. coli strain EP432 (ΔEG10652 "nhaA" ΔEG11392 "nhaB) which lacks Na+:H+ antiporter activity . The E. coli K-12 mutant strain KNabc (ΔnhaA ΔnhaB ΔchaA) cannot export Na+ and is unable to grow in the presence of of 0...

## Biological Role

Catalyzes sodium:proton antiport (reaction.ecocyc.TRANS-RXN-101), potassium:proton antiport (reaction.ecocyc.TRANS-RXN-42).

## Annotation

FUNCTION: Sodium exporter that functions mainly at alkaline pH (PubMed:8021217, PubMed:8496184, PubMed:9518629). Can also function as a potassium/proton and calcium/proton antiporter at alkaline pH (PubMed:16687400, PubMed:18342619, PubMed:8021217, PubMed:8496184). Does not play a major role in calcium export (PubMed:18342619). The K(+)/H(+) antiporter activity may enable E.coli to adapt to K(+) salinity stress and to maintain K(+) homeostasis (PubMed:16687400). {ECO:0000269|PubMed:16687400, ECO:0000269|PubMed:18342619, ECO:0000269|PubMed:8021217, ECO:0000269|PubMed:8496184, ECO:0000269|PubMed:9518629}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-101|reaction.ecocyc.TRANS-RXN-101]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-42|reaction.ecocyc.TRANS-RXN-42]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1216|gene.b1216]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31801`
- `KEGG:ecj:JW1207;eco:b1216;ecoc:C3026_07155;`
- `GeneID:945790;`
- `GO:GO:0005886; GO:0010446; GO:0015385; GO:0015386`

## Notes

Sodium-potassium/proton antiporter ChaA (Na(+)/H(+) exchanger)
