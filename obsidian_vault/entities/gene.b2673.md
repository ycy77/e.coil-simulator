---
entity_id: "gene.b2673"
entity_type: "gene"
name: "nrdH"
source_database: "NCBI RefSeq"
source_id: "gene-b2673"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2673"
  - "nrdH"
---

# nrdH

`gene.b2673`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2673`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nrdH (gene.b2673) is a gene entity. It encodes nrdH (protein.P0AC65). Encoded protein function: FUNCTION: Electron transport system for the ribonucleotide reductase system NrdEF. EcoCyc product frame: G7401-MONOMER. EcoCyc synonyms: ygaN. Genomic coordinates: 2800723-2800968. EcoCyc protein note: NrdH is an electron donor for RIBONUCLEOSIDE-DIP-REDUCTII-CPLX . It has higher specificity for the class Ib (NrdEF) enzyme than for the class Ia (NrdAB) enzyme. NrdH itself is reduced by thioredoxin reductase, but not by glutathione. The redox potential of NrdH is 248.5 mV . NrdH behaves functionally like a classical thioredoxin, but has sequence similarity to glutaredoxins . A crystal structure of NrdH in the oxidized state has been determined at 1.7 Å resolution, showing that the protein is structurally similar to glutaredoxin 3. However, the glutathione-binding cleft is absent, and NrdH instead contains a thioredoxin-like hydrophobic pocket at the surface, which may allow it to interact with thioredoxin reductase . Expression of the nrdHIEF operon is increased by hydroxyurea and oxidative stress . Expression is highest in minimal medium and in early log phase growth in complex medium; deletion of Trx1 and Grx1 (trxA- grxA-) increases expression more than 100-fold . nrdHIEF belongs to the Fur regulon .

## Biological Role

Repressed by [2Fe-2S] cluster DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-7639), nrdR (protein.P0A8D0), fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC65|protein.P0AC65]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=nrdH; function=+
- `represses` <-- [[complex.ecocyc.CPLX0-7639|complex.ecocyc.CPLX0-7639]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A8D0|protein.P0A8D0]] `RegulonDB` `S` - regulator=NrdR; target=nrdH; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=nrdH; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008802,ECOCYC:G7401,GeneID:947161`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2800723-2800968:+; feature_type=gene
