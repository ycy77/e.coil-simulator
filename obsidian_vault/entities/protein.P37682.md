---
entity_id: "protein.P37682"
entity_type: "protein"
name: "yiaU"
source_database: "UniProt"
source_id: "P37682"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yiaU b3585 JW3557"
---

# yiaU

`protein.P37682`

## Static

- Type: `protein`
- Source: `UniProt:P37682`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

Uncharacterized HTH-type transcriptional regulator YiaU YiaU is a LysR-type transcription factor involved in regulation of bacterial envelope biogenesis, antibiotic resistance, biofilm formation, and complement sensitivity . This protein contains a helix-turn-helix motif to bind DNA in its N-terminal domain, and it was predicted to regulate genes related to toxins and cell fitness . In systematic studies of oligomerization, it was shown that some members of the LysR family, like YiaU, interact with other members of the family to form heterodimers, but the physiological significance of this is unknown . Genome-wide YiaU binding sites were determined in vivo by the chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium , and in vitro by genomic systematic evolution of ligands using exponential enrichment (gSELEX-chip) . A total of five YiaU binding regions were identified by gSELEX-chip and confirmed by gel shift assay; these binding regions flank six operons encoding envelope components or proteins involved in its modification . The in vivo transcriptional regulation of some of the binding targets identified by gSELEX-chip was determined by RT-qPCR. A YiaU binding site was identified by gSELEX-chip in the yiaU-yiaT spacer, suggesting autoregulation...

## Annotation

Uncharacterized HTH-type transcriptional regulator YiaU

## Outgoing Edges (6)

- `activates` --> [[gene.b3213|gene.b3213]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3584|gene.b3584]] `RegulonDB|EcoCyc` `C` - regulator=YiaU; target=yiaT; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3586|gene.b3586]] `RegulonDB` `C` - regulator=YiaU; target=yiaV; function=+
- `activates` --> [[gene.b3587|gene.b3587]] `RegulonDB` `C` - regulator=YiaU; target=yiaW; function=+
- `activates` --> [[gene.b3630|gene.b3630]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b3714|gene.b3714]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## Incoming Edges (1)

- `encodes` <-- [[gene.b3585|gene.b3585]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37682`
- `KEGG:ecj:JW3557;eco:b3585;ecoc:C3026_19435;`
- `GeneID:948107;`
- `GO:GO:0003700; GO:0005829; GO:0006355; GO:0043565`

## Notes

Uncharacterized HTH-type transcriptional regulator YiaU
