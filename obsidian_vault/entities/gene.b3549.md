---
entity_id: "gene.b3549"
entity_type: "gene"
name: "tag"
source_database: "NCBI RefSeq"
source_id: "gene-b3549"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3549"
  - "tag"
---

# tag

`gene.b3549`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3549`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tag (gene.b3549) is a gene entity. It encodes tag (protein.P05100). Encoded protein function: FUNCTION: Hydrolysis of the deoxyribose N-glycosidic bond to excise 3-methyladenine from the damaged DNA polymer formed by alkylation lesions. {ECO:0000269|PubMed:3536912}. EcoCyc product frame: EG10986-MONOMER. EcoCyc synonyms: tagA. Genomic coordinates: 3713092-3713655. EcoCyc protein note: Alkylating agents such as N-methyl-N'-nitro-N-nitrosoguanidine (MNNG) or methyl methanesulfonate (MMS) can produce potentially mutagenic lesions in DNA. Alkylation damage may also occur spontaneously in living organisms through the action of methyl donors such as S-adenosylmethionine . The product of the tag gene in Escherichia coli is one of two (along with AlkA) 3-methyladenine-DNA-glycosylases present in the genome. Like AlkA, it acts preferentially on double-stranded DNA containing 3-methyladenine by catalyzing the hydrolysis of the N-glycosylic bonds linking the methylated base to the deoxyribose -phosphate backbone. This enzymatic action results in the formation of an apurinic (AP) site which requires further repair through the action of an AP endonuclease, DNA polymerase and DNA-ligase. Unlike AlkA, the tag gene product is not inducible through the adaptation response.

## Enriched Pathways

- `eco03410` Base excision repair (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P05100|protein.P05100]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0011593,ECOCYC:EG10986,GeneID:947137`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3713092-3713655:+; feature_type=gene
