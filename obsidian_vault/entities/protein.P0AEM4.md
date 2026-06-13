---
entity_id: "protein.P0AEM4"
entity_type: "protein"
name: "flgM"
source_database: "UniProt"
source_id: "P0AEM4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "flgM b1071 JW1058"
---

# flgM

`protein.P0AEM4`

## Static

- Type: `protein`
- Source: `UniProt:P0AEM4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for the coupling of flagellin expression to flagellar assembly by preventing expression of the flagellin genes when a component of the middle class of proteins is defective. It negatively regulates flagellar genes by inhibiting the activity of FliA by directly binding to FliA. FlgM is an anti-sigma factor that protects its corresponding sigma factor, σ28 (EG11355-MONOMER FliA), against degradation by the Lon protease . FlgM is an intrinsically disordered protein that exists in a pre-molten globule-like conformation . FlgM function has been extensively studied in Salmonella typhimurium. FlgM is an intrinsically disordered protein that becomes structured on binding to the transcription factor σ28, regulating flagellar synthesis . FlgM is produced from both the class 2 transcript of flgAMN and the class 3 transcript of flgMN. FlgM is initially translated from its class 2, FlhDC-activated, σ70-dependent transcript. FlgM is the anti-σ28 factor responsible for regulation of σ28 activity and functions in coupling of flagellar assembly to gene expression. FlgM prevents σ28 from binding to DNA by interacting with its promoter -binding domain. Once the hook-basal body structure of the flagellum is complete, the cell becomes capable of flagellum-specific type III secretion of FlgM, and it is secreted...

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Annotation

FUNCTION: Responsible for the coupling of flagellin expression to flagellar assembly by preventing expression of the flagellin genes when a component of the middle class of proteins is defective. It negatively regulates flagellar genes by inhibiting the activity of FliA by directly binding to FliA.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)
- `eco02040` Flagellar assembly (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1071|gene.b1071]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEM4`
- `KEGG:ecj:JW1058;eco:b1071;ecoc:C3026_06500;`
- `GeneID:75171196;75203658;946684;`
- `GO:GO:0016989; GO:0044781; GO:0045861`

## Notes

Negative regulator of flagellin synthesis (Anti-sigma-28 factor)
