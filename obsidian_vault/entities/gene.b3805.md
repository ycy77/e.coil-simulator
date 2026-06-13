---
entity_id: "gene.b3805"
entity_type: "gene"
name: "hemC"
source_database: "NCBI RefSeq"
source_id: "gene-b3805"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3805"
  - "hemC"
---

# hemC

`gene.b3805`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3805`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hemC (gene.b3805) is a gene entity. It encodes hemC (protein.P06983). Encoded protein function: FUNCTION: Tetrapolymerization of the monopyrrole PBG into the hydroxymethylbilane pre-uroporphyrinogen in several discrete steps. {ECO:0000269|PubMed:3529035}. EcoCyc product frame: OHMETHYLBILANESYN-MONOMER. EcoCyc synonyms: popE. Genomic coordinates: 3989825-3990766. EcoCyc protein note: Hydroxymethylbilane synthase (HMBS) catalyzes the tetrapolymerization of porphobilinogen yielding the linear tetrapyrrole hydroxymethylbilane (preuroporphyrinogen) which is highly unstable. With uroporphyrinogen III synthase, the product cyclizes to the next intermediate, uroporphyrinogen III. In the absence of the next enzyme in the pathway, the product spontaneously cyclizes to form uroporphyrinogen I, which is not a normal metabolite. HMBS and uroporphyrinogen III synthase form a complex . HMBS contains a covalently bound dipyrromethane (dipyrrole) that is an essential cofactor for enzyme activity. The cofactor is bound irreversibly to cysteine-242 . The crystal structure of the enzyme has been determined up to 1.7 Å resolution . Site directed mutagenesis studies have been carried out in the catalytic cleft . Asp-84 has been shown to be a critical catalytic residue, substitution results in an almost inactive enzyme .

## Enriched Pathways

- `eco00860` Porphyrin metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06983|protein.P06983]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012427,ECOCYC:EG10429,GeneID:947759`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3989825-3990766:-; feature_type=gene
