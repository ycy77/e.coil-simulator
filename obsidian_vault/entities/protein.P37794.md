---
entity_id: "protein.P37794"
entity_type: "protein"
name: "chbG"
source_database: "UniProt"
source_id: "P37794"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:22797760}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "chbG ydjC b1733 JW1722"
---

# chbG

`protein.P37794`

## Static

- Type: `protein`
- Source: `UniProt:P37794`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:22797760}.

## Enriched Summary

FUNCTION: ChbG is essential for growth on the acetylated chitooligosaccharides chitobiose and chitotriose but is dispensable for growth on cellobiose and chitosan dimer, the deacetylated form of chitobiose. Deacetylation of chitobiose-6-P and chitotriose-6-P is necessary for both the activation of the chb promoter by the regulatory protein ChbR and the hydrolysis of phosphorylated beta-glucosides by the phospho-beta-glucosidase ChbF. Catalyzes the removal of only one acetyl group from chitobiose-6-P to yield monoacetylchitobiose-6-P, the inducer of ChbR and the substrate of ChbF. It can also use chitobiose and chitotriose as substrates. {ECO:0000269|PubMed:22797760}. ChbG is a chitooligosaccharide monodeacetylase encoded as part of the chb operon, which encodes enzymes involved in growth on CHITOBIOSE as the sole source of carbon . A ΔchbG strain is unable to grow on diacetylchitobiose or triacetylchitobiose as the sole source of carbon and energy. A ΔchbF mutant accumulates monoacetylchitobiose-phosphate; recombinant ChbF degrades this accumulated compound to glucosamine-6-phosphate and N-acetylglucosamine. This, together with additional evidence, shows that ChbG deacetylates diacetylchitobiose at the non-reducing (phosphorylated) end . Mutations in conserved residues of a predicted metal binding site negatively affect the activity of ChbG...

## Biological Role

Catalyzes RXN0-7391 (reaction.ecocyc.RXN0-7391).

## Annotation

FUNCTION: ChbG is essential for growth on the acetylated chitooligosaccharides chitobiose and chitotriose but is dispensable for growth on cellobiose and chitosan dimer, the deacetylated form of chitobiose. Deacetylation of chitobiose-6-P and chitotriose-6-P is necessary for both the activation of the chb promoter by the regulatory protein ChbR and the hydrolysis of phosphorylated beta-glucosides by the phospho-beta-glucosidase ChbF. Catalyzes the removal of only one acetyl group from chitobiose-6-P to yield monoacetylchitobiose-6-P, the inducer of ChbR and the substrate of ChbF. It can also use chitobiose and chitotriose as substrates. {ECO:0000269|PubMed:22797760}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-7391|reaction.ecocyc.RXN0-7391]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1733|gene.b1733]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37794`
- `KEGG:ecj:JW1722;eco:b1733;ecoc:C3026_09905;`
- `GeneID:946231;`
- `GO:GO:0000272; GO:0005737; GO:0006032; GO:0019213; GO:0036311; GO:0046872; GO:0052773; GO:0052777`
- `EC:3.5.1.105`

## Notes

Chitooligosaccharide deacetylase ChbG (COD) (EC 3.5.1.105) (Chitin disaccharide deacetylase) (Chitobiose deacetylase) (Chitobiose-6P deacetylase) (Chitotriose deacetylase) (Chitotriose-6P deacetylase)
