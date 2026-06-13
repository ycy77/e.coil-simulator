---
entity_id: "gene.b2942"
entity_type: "gene"
name: "metK"
source_database: "NCBI RefSeq"
source_id: "gene-b2942"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2942"
  - "metK"
---

# metK

`gene.b2942`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2942`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metK (gene.b2942) is a gene entity. It encodes metK (protein.P0A817). Encoded protein function: FUNCTION: Catalyzes the formation of S-adenosylmethionine (AdoMet) from methionine and ATP. The overall synthetic reaction is composed of two sequential steps, AdoMet formation and the subsequent tripolyphosphate hydrolysis which occurs prior to release of AdoMet from the enzyme (PubMed:10551856, PubMed:10660564, PubMed:6251075, PubMed:7629147, PubMed:7629176, PubMed:9753435). Is essential for growth (PubMed:11952912). {ECO:0000269|PubMed:10551856, ECO:0000269|PubMed:10660564, ECO:0000269|PubMed:11952912, ECO:0000269|PubMed:6251075, ECO:0000269|PubMed:7629147, ECO:0000269|PubMed:7629176, ECO:0000269|PubMed:9753435}. EcoCyc product frame: S-ADENMETSYN-MONOMER. EcoCyc synonyms: metX. Genomic coordinates: 3086706-3087860. EcoCyc protein note: Methionine adenosyltransferase catalyzes the formation of the sulfonium compound S-adenosylmethionine. The reaction is unusual in that the entire tripolyphosphate chain is cleaved from the ATP molecule, and is further degraded to pyrophosphate and phosphate before the products are released . Due to its importance, the enzyme is a target for the development of antimicrobial and anticancer compounds. The enzyme is a homotetramer in solution ; the tetrameric form is required for activity...

## Biological Role

Repressed by lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), rpoS (protein.P13445).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A817|protein.P0A817]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=metK; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=metK; function=+
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB|EcoCyc` `S` - regulator=Lrp; target=metK; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0009650,ECOCYC:EG10589,GeneID:945389`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3086706-3087860:+; feature_type=gene
