---
entity_id: "gene.b1701"
entity_type: "gene"
name: "fadK"
source_database: "NCBI RefSeq"
source_id: "gene-b1701"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1701"
  - "fadK"
---

# fadK

`gene.b1701`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1701`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fadK (gene.b1701) is a gene entity. It encodes fadK (protein.P38135). Encoded protein function: FUNCTION: Catalyzes the esterification, concomitant with transport, of exogenous fatty acids into metabolically active CoA thioesters for subsequent degradation or incorporation into phospholipids. Is maximally active on C6:0, C8:0 and C12:0 fatty acids, while has a low activity on C14-C18 chain length fatty acids (PubMed:15213221, PubMed:19477415). Is involved in the anaerobic beta-oxidative degradation of fatty acids, which allows anaerobic growth of E.coli on fatty acids as a sole carbon and energy source in the presence of nitrate or fumarate as a terminal electron acceptor (PubMed:12535077). Can functionally replace FadD under anaerobic conditions (PubMed:12535077). {ECO:0000269|PubMed:12535077, ECO:0000269|PubMed:15213221, ECO:0000269|PubMed:19477415}. EcoCyc product frame: EG12357-MONOMER. EcoCyc synonyms: ydiD. Genomic coordinates: 1782977-1784677. EcoCyc protein note: FadK is an acyl-CoA synthetase that is primarily active on medium-chain (C6:0 and C8:0) fatty acids and acts in anaerobic β-oxidation of fatty acids . During anaerobic β-oxidation of fatty acids, G7213 FadI, G7212 FadJ, and EG12357 FadK serve functions parallel to those of EG10278 FadA, EG10279 FadB, and EG11530 FadD in the aerobic pathway...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P38135|protein.P38135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0005676,ECOCYC:EG12357,GeneID:946213`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1782977-1784677:+; feature_type=gene
