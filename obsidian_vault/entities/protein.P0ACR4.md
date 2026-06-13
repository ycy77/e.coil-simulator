---
entity_id: "protein.P0ACR4"
entity_type: "protein"
name: "yeiE"
source_database: "UniProt"
source_id: "P0ACR4"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yeiE b2157 JW2144"
---

# yeiE

`protein.P0ACR4`

## Static

- Type: `protein`
- Source: `UniProt:P0ACR4`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcription factor, which is probably involved in maintaining iron homeostasis under iron-limited conditions (PubMed:30137486). It shows over 100 binding sites across the E.coli K12 MG1655 genome (PubMed:30137486). Target genes are involved in diverse biological processes, including transport and metabolism, cell wall/membrane biogenesis, signal transduction and transcriptional regulation, suggesting that YeiE may play multiple biological roles (PubMed:30137486). It may function as a positive regulator of lysP expression, leading to the increase of lysine uptake (PubMed:12400704). {ECO:0000269|PubMed:12400704, ECO:0000269|PubMed:30137486}. YeiE is a LysR-related protein that appears to activate transcription of lysP . YeiE was confirmed as a TF through an integrated workflow comprised of computational prediction, knowledge-based classification, and experimental validation of candidate TFs at the genome scale . YeiE is involved in iron uptake under iron-limited conditions . Expression of yeiE increases yield from a strain engineered to produce L-pipecolic acid from L-lysine . Compared to known global TFs, YeiE exhibits some interesting regulatory features. First, it has more intragenic binding peaks and fewer peaks located within putative regulatory regions. Second, it has fewer binding peaks than global TFs, such as CRP, Lrp, Fnr, and ArcA...

## Annotation

FUNCTION: Transcription factor, which is probably involved in maintaining iron homeostasis under iron-limited conditions (PubMed:30137486). It shows over 100 binding sites across the E.coli K12 MG1655 genome (PubMed:30137486). Target genes are involved in diverse biological processes, including transport and metabolism, cell wall/membrane biogenesis, signal transduction and transcriptional regulation, suggesting that YeiE may play multiple biological roles (PubMed:30137486). It may function as a positive regulator of lysP expression, leading to the increase of lysine uptake (PubMed:12400704). {ECO:0000269|PubMed:12400704, ECO:0000269|PubMed:30137486}.

## Outgoing Edges (15)

- `activates` --> [[gene.b1376|gene.b1376]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1646|gene.b1646]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1810|gene.b1810]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3214|gene.b3214]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0621|gene.b0621]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0884|gene.b0884]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0903|gene.b0903]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b0936|gene.b0936]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1014|gene.b1014]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1441|gene.b1441]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2214|gene.b2214]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2764|gene.b2764]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b2923|gene.b2923]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3514|gene.b3514]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3614|gene.b3614]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b2157|gene.b2157]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACR4`
- `KEGG:ecj:JW2144;eco:b2157;ecoc:C3026_12090;`
- `GeneID:93775025;946657;`
- `GO:GO:0000976; GO:0003700; GO:0006351; GO:0006355`

## Notes

HTH-type transcriptional regulator YeiE
