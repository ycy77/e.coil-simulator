---
entity_id: "gene.b2236"
entity_type: "gene"
name: "yfaE"
source_database: "NCBI RefSeq"
source_id: "gene-b2236"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2236"
  - "yfaE"
---

# yfaE

`gene.b2236`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2236`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfaE (gene.b2236) is a gene entity. It encodes yfaE (protein.P0ABW3). Encoded protein function: Uncharacterized ferredoxin-like protein YfaE EcoCyc product frame: EG12360-MONOMER. Genomic coordinates: 2348514-2348768. EcoCyc protein note: YfaE is a [2Fe-2S] cluster-containing protein that is involved in maintenance and possibly in the biosynthesis of active B2-CPLX "NrdB β2 subunit" containing the diferric-tyrosyl radical (Y·) cofactor within ribonucleotide reductase . YfaE is required for the activity of β during redox stress at high Mn2+ conditions and may provide metal specificity to NrdB . YfaE was purified from inclusion bodies and refolded/reassembled by addition of Fe2+, Fe3+ and sulfide under anaerobic conditions. The oxidized form of YfaE is not stable and forms aggregates . A ΔyfaE mutant has aggravating genetic interactions with genes involved in DNA metabolism . Review:

## Biological Role

Repressed by dnaA (protein.P03004), nrdR (protein.P0A8D0), hns (protein.P0ACF8), nac (protein.Q47005). Activated by dnaA (protein.P03004), fis (protein.P0A6R3), argP (protein.P0A8S1).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABW3|protein.P0ABW3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=yfaE; function=-+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=yfaE; function=+
- `activates` <-- [[protein.P0A8S1|protein.P0A8S1]] `RegulonDB` `S` - regulator=ArgP; target=yfaE; function=+
- `represses` <-- [[protein.P03004|protein.P03004]] `RegulonDB` `C` - regulator=DnaA; target=yfaE; function=-+
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=yfaE; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=yfaE; function=-
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yfaE; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007390,ECOCYC:EG12360,GeneID:946729`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2348514-2348768:+; feature_type=gene
