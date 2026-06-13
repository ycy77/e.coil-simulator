---
entity_id: "gene.b3635"
entity_type: "gene"
name: "mutM"
source_database: "NCBI RefSeq"
source_id: "gene-b3635"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3635"
  - "mutM"
---

# mutM

`gene.b3635`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3635`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mutM (gene.b3635) is a gene entity. It encodes mutM (protein.P05523). Encoded protein function: FUNCTION: Involved in base excision repair of DNA damaged by oxidation or by mutagenic agents. Acts as a DNA glycosylase that recognizes and removes damaged bases. Has a preference for oxidized purines, such as 7,8-dihydro-8-oxoguanine (8-oxoG) and its derivatives such as guanidinohydantoin:C and spiroiminodihydantoin:C, however it also acts on thymine glycol:G, 5,6-dihydrouracil:G and 5-hydroxyuracil:G. Has AP (apurinic/apyrimidinic) lyase activity and introduces nicks in the DNA strand. Cleaves the DNA backbone by beta-delta elimination to generate a single-strand break at the site of the removed base with both 3'- and 5'-phosphates. Cleaves ssDNA containing an AP site. {ECO:0000269|PubMed:1689309, ECO:0000269|PubMed:20031487}. EcoCyc product frame: EG10329-MONOMER. EcoCyc synonyms: fpg. Genomic coordinates: 3810343-3811152. EcoCyc protein note: MutM (also known as Fpg or formamidopyrimidine glycosylase) is a bifunctional DNA glycosylase which cleaves the N-glycosidic bond of redox-damaged purines and incises the phosphodiester backbone to yield single strand breaks with 3' and 5'-phosphoryl ends; the reaction proceeds via formation of an enzyme-substrate Schiff base intermediate with subsequent β,δ-elimination reactions (see )...

## Biological Role

Repressed by rpoN (protein.P24255). Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05523|protein.P05523]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=mutM; function=+
- `represses` <-- [[protein.P24255|protein.P24255]] `RegulonDB|EcoCyc` `S` - regulator=RpoN; target=mutM; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0011877,ECOCYC:EG10329,GeneID:946765`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3810343-3811152:-; feature_type=gene
