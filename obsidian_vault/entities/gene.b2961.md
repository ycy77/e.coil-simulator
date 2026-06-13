---
entity_id: "gene.b2961"
entity_type: "gene"
name: "mutY"
source_database: "NCBI RefSeq"
source_id: "gene-b2961"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2961"
  - "mutY"
---

# mutY

`gene.b2961`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2961`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mutY (gene.b2961) is a gene entity. It encodes mutY (protein.P17802). Encoded protein function: FUNCTION: Adenine glycosylase active on G-A mispairs. MutY also corrects error-prone DNA synthesis past GO lesions which are due to the oxidatively damaged form of guanine: 7,8-dihydro-8-oxoguanine (8-oxo-dGTP). {ECO:0000269|PubMed:1445834, ECO:0000269|PubMed:2682664}. EcoCyc product frame: EG10627-MONOMER. EcoCyc synonyms: micA. Genomic coordinates: 3103013-3104065. EcoCyc protein note: MutY is a novel base excision repair (BER) glycosylase which catalyses the removal of adenine when it is paired with the oxidatively damaged form of guanine, CPD-12427 (GO; 8-oxoG); MutY activity prevents deleterious G:C → T:A transversion mutations. Strains defective in MutY function stimulate G:C → T:A transversion (see also ). Purified MutY is an A:G specific adenine glycosylase; MutY, a 5' endonuclease, and DNA polymerase I are able to reconstitute A:G → C:G mismatch correction in vitro . MutY removes adenines from 8-oxoG:A mispairs that result from trans-lesion DNA replication past 8-oxoG; MutY also removes adenine from A:C, and A:8-oxo-7,8-dihydrodeoxyadenine mispairs; MutY remains bound to the repair site which may prevent MutM from removing the 8-oxoG lesion with subsequent double strand break . MutY may or may not have associated apurinic/apyrimidinic endonuclease activity (see also )...

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P17802|protein.P17802]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009720,ECOCYC:EG10627,GeneID:947447`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3103013-3104065:+; feature_type=gene
