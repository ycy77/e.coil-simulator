---
entity_id: "protein.P76340"
entity_type: "protein"
name: "hprR"
source_database: "UniProt"
source_id: "P76340"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hprR yedW b1969 JW5322"
---

# hprR

`protein.P76340`

## Static

- Type: `protein`
- Source: `UniProt:P76340`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Member of a two-component regulatory system HprR/HprS involved in response to hydrogen peroxide (PubMed:25568260, PubMed:27983483). Regulates the expression of at least 5 operons, cyoABCDE, hprRS, hiuH, cusRS and cusCFBA. Bifunctional regulator that acts as an activator and a repressor (PubMed:25568260). {ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}. Based on Genomic SELEX screening, the two-component system (TCS) HprSR (previously called YedVW) has been characterized, and five operons, cyoABCDE, yedVW, hiuH, cusSR, and cusCFBA, were predicted to be under the direct control of this TCS; however, its regulatory role has only been examined for the hiuH gene . On the other hand, Shimada et al. reported, also based on Genomic SELEX screening, that HrpR binds strongly only between the TU0-1822 and TU0-1821 operons and that with minor strength HprR binds between TU0-13468 and hprR genes; these authors classified this protein as a single-target transcription factor . Genome-wide HprR binding sites were also determined in vivo by chromatin immunoprecipitation method combined with lambda exonuclease digestion (ChIP-exo) in glucose M9 minimal medium . The sensor of the HprSR TCS, HprS, responds to reactive chlorine species (RCS)...

## Annotation

FUNCTION: Member of a two-component regulatory system HprR/HprS involved in response to hydrogen peroxide (PubMed:25568260, PubMed:27983483). Regulates the expression of at least 5 operons, cyoABCDE, hprRS, hiuH, cusRS and cusCFBA. Bifunctional regulator that acts as an activator and a repressor (PubMed:25568260). {ECO:0000269|PubMed:25568260, ECO:0000269|PubMed:27983483}.

## Outgoing Edges (9)

- `activates` --> [[gene.b0570|gene.b0570]] `RegulonDB` `S` - regulator=HprR; target=cusS; function=+
- `activates` --> [[gene.b0571|gene.b0571]] `RegulonDB` `S` - regulator=HprR; target=cusR; function=+
- `activates` --> [[gene.b0572|gene.b0572]] `RegulonDB` `S` - regulator=HprR; target=cusC; function=+
- `activates` --> [[gene.b0573|gene.b0573]] `RegulonDB` `S` - regulator=HprR; target=cusF; function=+
- `activates` --> [[gene.b0574|gene.b0574]] `RegulonDB` `S` - regulator=HprR; target=cusB; function=+
- `activates` --> [[gene.b0575|gene.b0575]] `RegulonDB` `S` - regulator=HprR; target=cusA; function=+
- `activates` --> [[gene.b1970|gene.b1970]] `RegulonDB` `C` - regulator=HprR; target=hiuH; function=+
- `activates` --> [[gene.b1971|gene.b1971]] `RegulonDB` `C` - regulator=HprR; target=msrP; function=+
- `activates` --> [[gene.b1972|gene.b1972]] `RegulonDB` `C` - regulator=HprR; target=msrQ; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b1969|gene.b1969]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76340`
- `KEGG:ecj:JW5322;eco:b1969;ecoc:C3026_11125;`
- `GeneID:946486;`
- `GO:GO:0000156; GO:0000976; GO:0003677; GO:0003700; GO:0005829; GO:0006355; GO:0032993; GO:0045892; GO:0045893`

## Notes

Transcriptional regulatory protein HprR (Hydrogen peroxide response regulator)
