---
entity_id: "gene.b2551"
entity_type: "gene"
name: "glyA"
source_database: "NCBI RefSeq"
source_id: "gene-b2551"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2551"
  - "glyA"
---

# glyA

`gene.b2551`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2551`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glyA (gene.b2551) is a gene entity. It encodes glyA (protein.P0A825). Encoded protein function: FUNCTION: Catalyzes the reversible interconversion of serine and glycine with tetrahydrofolate (THF) serving as the one-carbon carrier. This reaction serves as the major source of one-carbon groups required for the biosynthesis of purines, thymidylate, methionine, and other important biomolecules (PubMed:10858298, PubMed:1517215, PubMed:19883126, PubMed:3891721, PubMed:7925461). Also exhibits THF-independent aldolase activity toward beta-hydroxyamino acids, producing glycine and aldehydes, via a retro-aldol mechanism. Thus, is able to catalyze the cleavage of allothreonine and 3-phenylserine (PubMed:10858298, PubMed:1517215, PubMed:19883126, PubMed:3891721). Also catalyzes the irreversible conversion of 5,10-methenyltetrahydrofolate to 5-formyltetrahydrofolate (PubMed:10858298, PubMed:2201683). {ECO:0000269|PubMed:10858298, ECO:0000269|PubMed:1517215, ECO:0000269|PubMed:19883126, ECO:0000269|PubMed:2201683, ECO:0000269|PubMed:3891721, ECO:0000269|PubMed:7925461}. EcoCyc product frame: GLYOHMETRANS-MONOMER. Genomic coordinates: 2684254-2685507. EcoCyc protein note: Serine hydroxymethyltransferase (GlyA) converts L-serine (but not D-serine ) to glycine, transferring a methyl group to tetrahydrofolate, thus forming 5,10-methylene-tetrahydrofolate (5,10-mTHF)...

## Biological Role

Repressed by metR (protein.P0A9F9), purR (protein.P0ACP7). Activated by rpoD (protein.P00579), metR (protein.P0A9F9).

## Enriched Pathways

- `eco00260` Glycine, serine and threonine metabolism (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00630` Glyoxylate and dicarboxylate metabolism (KEGG)
- `eco00670` One carbon pool by folate (KEGG)
- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A825|protein.P0A825]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=glyA; function=+
- `activates` <-- [[protein.P0A9F9|protein.P0A9F9]] `RegulonDB` `C` - regulator=MetR; target=glyA; function=-+
- `represses` <-- [[protein.P0A9F9|protein.P0A9F9]] `RegulonDB` `C` - regulator=MetR; target=glyA; function=-+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `C` - regulator=PurR; target=glyA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008389,ECOCYC:EG10408,GeneID:947022`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2684254-2685507:-; feature_type=gene
