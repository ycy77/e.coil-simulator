---
entity_id: "gene.b1166"
entity_type: "gene"
name: "ariR"
source_database: "NCBI RefSeq"
source_id: "gene-b1166"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1166"
  - "ariR"
---

# ariR

`gene.b1166`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1166`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ariR (gene.b1166) is a gene entity. It encodes ariR (protein.P75993). Encoded protein function: FUNCTION: Probably a connector protein for RcsB/C regulation of biofilm and acid-resistance, providing additional signal input into the two-component signaling pathway. May serve to stimulate biofilm maturation, via the Rcs phosphorelay. Regulates expression of genes involved in acid-resistance and biofilm formation, including the RcsB/C two-component system. May be a non-specific DNA-binding protein that binds genes and/or intergenic regions via a geometric recognition. Also confers resistance to H(2)O(2). Overexpression at 28 and 16 degrees Celsius increases the production of colanic acid, an exopolysaccharide and matrix component, and reduces adhesive curli fimbriae expression. Both of these effects require RcsB; AriR probably acts upstream of the RcsB/C system to stimulate the activity and not transcription of RcsB/C. 5-fluorouracil reduction in biofilm formation requires this protein. {ECO:0000269|PubMed:17765265}. EcoCyc product frame: G6606-MONOMER. EcoCyc synonyms: ymgB. Genomic coordinates: 1216369-1216635. EcoCyc protein note: AriR appears to be a regulator of acid resistance and biofilm formation. AriR binds DNA, and in vivo target sites were identified by nickel-enrichment DNA microarray studies. In vitro, AriR binds DNA non-specifically...

## Biological Role

Repressed by bluR (protein.P75989). Activated by rpoD (protein.P00579), marA (protein.P0ACH5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75993|protein.P75993]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ariR; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=ariR; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ariR; function=+
- `represses` <-- [[protein.P75989|protein.P75989]] `RegulonDB` `C` - regulator=BluR; target=ariR; function=-

## External IDs

- `Dbxref:ECOCYC:G6606,GeneID:945340`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1216369-1216635:+; feature_type=gene
