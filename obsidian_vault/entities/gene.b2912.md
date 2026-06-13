---
entity_id: "gene.b2912"
entity_type: "gene"
name: "fau"
source_database: "NCBI RefSeq"
source_id: "gene-b2912"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2912"
  - "fau"
---

# fau

`gene.b2912`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2912`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fau (gene.b2912) is a gene entity. It encodes ygfA (protein.P0AC28). Encoded protein function: FUNCTION: Involved in the removal of 5-formyltetrahydrofolate. In vitro, it is a potent inhibitor of various folate-dependent enzymes in the C1 metabolism network and in vivo it might function as a folate storage. 5-formyltetrahydrofolate is also used as an antifolate rescue agent in cancer chemotherapy. Catalyzes the irreversible ATP-dependent transformation of 5-formyltetrahydrofolate (5-CHO-THF) to form 5,10-methenyltetrahydrofolate (5,10-CH=THF) (PubMed:20952389). The reverse reaction is catalyzed by the serine hydroxymethyltransferase GlyA (SHMT) (PubMed:20952389). {ECO:0000269|PubMed:18519731, ECO:0000269|PubMed:20952389, ECO:0000303|PubMed:20952389}. EcoCyc product frame: EG11158-MONOMER. EcoCyc synonyms: ygfA. Genomic coordinates: 3056241-3056789. EcoCyc protein note: The YgfA protein appears to be a 5-formyltetrahydrofolate (5-CHO-THF) cyclo-ligase. 5-CHO-THF is formed in a side reaction of GLYOHMETRANS-CPLX and is an inhibitor of various folate-dependent enzymes . ygfA is important for survival under competitive planktonic growth conditions and for formation of dormant persister cells . Overexpression of ygfA leads to increased tolerance to ofloxacin . Deletion of ygfA does not cause a growth defect in rich or minimal medium...

## Biological Role

Repressed by fis (protein.P0A6R3), hns (protein.P0ACF8), stpA (protein.P0ACG1), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), fis (protein.P0A6R3), rpoS (protein.P13445).

## Enriched Pathways

- `eco00670` One carbon pool by folate (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco04981` Folate transport and metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AC28|protein.P0AC28]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=fau; function=+
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fau; function=-+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=fau; function=+
- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=fau; function=-+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=fau; function=-
- `represses` <-- [[protein.P0ACG1|protein.P0ACG1]] `RegulonDB` `S` - regulator=StpA; target=fau; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=fau; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009559,ECOCYC:EG11158,GeneID:945167`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3056241-3056789:+; feature_type=gene
