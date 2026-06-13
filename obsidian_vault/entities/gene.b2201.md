---
entity_id: "gene.b2201"
entity_type: "gene"
name: "ccmA"
source_database: "NCBI RefSeq"
source_id: "gene-b2201"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2201"
  - "ccmA"
---

# ccmA

`gene.b2201`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2201`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmA (gene.b2201) is a gene entity. It encodes ccmA (protein.P33931). Encoded protein function: FUNCTION: Part of the ABC transporter complex CcmAB involved in the biogenesis of c-type cytochromes; once thought to export heme, this does not seem to be the case, but its exact role is uncertain. Responsible for energy coupling to the transport system. EcoCyc product frame: CCMA-MONOMER. EcoCyc synonyms: yejW. Genomic coordinates: 2297021-2297644. EcoCyc protein note: CcmA is the ATP-binding protein of a PWY-8147 "type I cytochrome c biogenesis system". ccmA is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmA deletion mutant cannot synthesize holocytochrome c but does produce heme-bound CCME-MONOMER CcmE (when CCMC-MONOMER CcmC is overproduced); CcmA and CCMB-MONOMER CcmB are implicated in heme transfer from holo-CcmE and attachment to apocytochrome c; CcmAB does not transport heme to the periplasm (and )...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33931|protein.P33931]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmA; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmA; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmA; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmA; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmA; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmA; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ccmA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007279,ECOCYC:EG12059,GeneID:946714`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2297021-2297644:-; feature_type=gene
