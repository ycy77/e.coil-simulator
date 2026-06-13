---
entity_id: "gene.b4279"
entity_type: "gene"
name: "nanX"
source_database: "NCBI RefSeq"
source_id: "gene-b4279"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4279"
  - "nanX"
---

# nanX

`gene.b4279`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4279`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

nanX (gene.b4279) is a gene entity. It encodes nanX (protein.P39352). Encoded protein function: FUNCTION: Probably transports across the inner membrane the two dehydrated forms of N-acetylneuraminate (Neu5Ac), 2,7-anhydro-N-acetylneuraminate (2,7-AN) and 2-deoxy-2,3-didehydro-N-acetylneuraminate (2,3-EN). {ECO:0000269|PubMed:32542330, ECO:0000269|PubMed:32669363}. EcoCyc product frame: YJHB-MONOMER. EcoCyc synonyms: yjhB. Genomic coordinates: 4504058-4505275. EcoCyc protein note: nanX encodes an inner membrane transporter that appears specific for CPD-6182 (2,7-AN) - a dehydrated form of the abundant sialic acid N-ACETYLNEURAMINATE "N-acetylneuraminate". In an engineered strain lacking sialic acid transporters and expressing the sialic acid utilisation pathway constitutively (E. coli BW25113 ΔnanT::FRT ΔnanX::F3 ΔnanR ΔnagC), the expression of recombinant NanX supports growth with 2,7-anhydro-N-acetylneuraminate as sole carbon source but does not support growth with CPD-23638 (2,3-EN) nor with N-acetylneuraminate . Deletion of nanX (in strain BW25113) results in complete loss of in vitro growth on 2,7-AN; NanX, functioning together with a co-expressed CPLX0-8544 hydratase, likely supports scavenging of 2,7-AN in the human gut (see also )...

## Biological Role

Repressed by nanR (protein.P0A8W0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39352|protein.P39352]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0A8W0|protein.P0A8W0]] `RegulonDB` `C` - regulator=NanR; target=nanX; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014025,ECOCYC:EG12544,GeneID:948807`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4504058-4505275:+; feature_type=gene
