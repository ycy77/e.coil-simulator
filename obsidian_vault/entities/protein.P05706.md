---
entity_id: "protein.P05706"
entity_type: "protein"
name: "srlB"
source_database: "UniProt"
source_id: "P05706"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:3553176}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "srlB gutB b2704 JW2673"
---

# srlB

`protein.P05706`

## Static

- Type: `protein`
- Source: `UniProt:P05706`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305|PubMed:3553176}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}. Contains a PTS Enzyme IIA (formerly Enzyme III) domain. The hydropathic profile of SrlB is typical of a soluble protein. SrlB may possess a net negative charge at neutral pH as predicted from it's amino acid sequence . srlB, among other genes involved in carbon source transport and metabolism, was downregulated in two MG1655 lysogens carrying closely related Stx2a phages O104 and PA8 .

## Biological Role

Catalyzes protein-N(pi)-phosphohistidine:D-sorbitol 6-phosphotransferase (reaction.R05820). Component of sorbitol-specific PTS enzyme II (complex.ecocyc.CPLX-169).

## Enriched Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II complex composed of SrlA, SrlB and SrlE is involved in glucitol/sorbitol transport. It can also use D-mannitol. {ECO:0000269|PubMed:1100608}.

## Pathways

- `eco00051` Fructose and mannose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R05820|reaction.R05820]] `KEGG` `database` - via EC:2.7.1.198
- `is_component_of` --> [[complex.ecocyc.CPLX-169|complex.ecocyc.CPLX-169]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2704|gene.b2704]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P05706`
- `KEGG:ecj:JW2673;eco:b2704;ecoc:C3026_14885;`
- `GeneID:948971;`
- `GO:GO:0005737; GO:0008982; GO:0009401; GO:0015795; GO:0016301; GO:0016773; GO:1902495`

## Notes

PTS system glucitol/sorbitol-specific EIIA component (EIIA-Gut) (EIII-Gut) (Glucitol/sorbitol-specific phosphotransferase enzyme IIA component)
