---
entity_id: "gene.b0382"
entity_type: "gene"
name: "iraP"
source_database: "NCBI RefSeq"
source_id: "gene-b0382"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0382"
  - "iraP"
---

# iraP

`gene.b0382`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0382`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

iraP (gene.b0382) is a gene entity. It encodes iraP (protein.P0AAN9). Encoded protein function: FUNCTION: Inhibits RpoS proteolysis by regulating RssB activity, thereby increasing the stability of the sigma stress factor RpoS especially during phosphate starvation, but also in stationary phase and during nitrogen starvation. Its effect on RpoS stability is due to its interaction with RssB, which probably blocks the interaction of RssB with RpoS, and the consequent delivery of the RssB-RpoS complex to the ClpXP protein degradation pathway. {ECO:0000269|PubMed:16600914, ECO:0000269|PubMed:18383615}. EcoCyc product frame: EG11256-MONOMER. EcoCyc synonyms: yaiB. Genomic coordinates: 401386-401646. EcoCyc protein note: IraP is one of several small anti-adaptor proteins; it is required for stabilization of the alternative sigma factor RPOS-MONOMER σS during phosphate starvation and plays a role in stationary phase and nitrogen starvation. The EG12121-MONOMER RssB adaptor protein binds to σS and targets it to the ClpXP protease for degradation. IraP does not affect the level or stability of RssB, but interferes directly with RssB-mediated degradation of σS by interacting with RssB . Each anti-adaptor protein interacts with RssB in a unique way . IraP does not inactivate ClpXP...

## Biological Role

Repressed by hns (protein.P0ACF8), nac (protein.Q47005). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), ydcI (protein.P77171).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AAN9|protein.P0AAN9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=iraP; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P77171|protein.P77171]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=iraP; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001313,ECOCYC:EG11256,GeneID:947709`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:401386-401646:+; feature_type=gene
