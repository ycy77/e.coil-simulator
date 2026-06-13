---
entity_id: "protein.P37595"
entity_type: "protein"
name: "iaaA"
source_database: "UniProt"
source_id: "P37595"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "iaaA spt ybiK b0828 JW0812"
---

# iaaA

`protein.P37595`

## Static

- Type: `protein`
- Source: `UniProt:P37595`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Degrades proteins damaged by L-isoaspartyl residue formation (also known as beta-Asp residues). Degrades L-isoaspartyl-containing di- and maybe also tripeptides. Also has L-asparaginase activity, although this may not be its principal function. {ECO:0000269|PubMed:11988085}.; FUNCTION: May be involved in glutathione, and possibly other peptide, transport, although these results could also be due to polar effects of disruption. {ECO:0000269|PubMed:11988085}.

## Biological Role

Catalyzes L-asparagine amidohydrolase (reaction.R00485). Component of isoaspartyl dipeptidase / asparaginase 3 (complex.ecocyc.CPLX0-263).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Degrades proteins damaged by L-isoaspartyl residue formation (also known as beta-Asp residues). Degrades L-isoaspartyl-containing di- and maybe also tripeptides. Also has L-asparaginase activity, although this may not be its principal function. {ECO:0000269|PubMed:11988085}.; FUNCTION: May be involved in glutathione, and possibly other peptide, transport, although these results could also be due to polar effects of disruption. {ECO:0000269|PubMed:11988085}.

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00485|reaction.R00485]] `KEGG` `database` - via EC:3.5.1.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-263|complex.ecocyc.CPLX0-263]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0828|gene.b0828]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37595`
- `KEGG:ecj:JW0812;eco:b0828;ecoc:C3026_05195;`
- `GeneID:945456;`
- `GO:GO:0004067; GO:0008798; GO:0016540; GO:0016787`
- `EC:3.4.19.5`

## Notes

Isoaspartyl peptidase (EC 3.4.19.5) (Beta-aspartyl-peptidase) (EcAIII) (Isoaspartyl dipeptidase) [Cleaved into: Isoaspartyl peptidase subunit alpha; Isoaspartyl peptidase subunit beta]
