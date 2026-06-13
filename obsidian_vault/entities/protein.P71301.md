---
entity_id: "protein.P71301"
entity_type: "protein"
name: "ecpR"
source_database: "UniProt"
source_id: "P71301"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ecpR matA ykgK b0294 JW5031"
---

# ecpR

`protein.P71301`

## Static

- Type: `protein`
- Source: `UniProt:P71301`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition. Positively regulates the expression of the ecp operon (By similarity). Also represses expression of the flagellar master operon flhDC, and consequently prevents flagellum biosynthesis and motility. Acts by binding to the regulatory region of the flhDC operon (Probable). {ECO:0000250, ECO:0000269|PubMed:22422754, ECO:0000305}. MatA is a LuxR-type transcription factor that is directly involved, as a positive regulator acting at transcriptional and posttranscriptional levels, in the expression of the mat operon in meningitis isolate strain IHE 3034 (T. A. Lehti, P. Bauchart, M. Kukkonen, U. Dobrindt, T. K. Korhonen, B. Westerlund-Wikstrom, unpublished results) . On the other hand, MatA controls the expression of the flhDC operon, with higher affinity to flhDp, repressing flagellum biosynthesis, motility, and taxis . The opposite regulatory actions of MatA on mat and on flhDC promoters advance the adaptation of E. coli from a planktonic to an adhesive lifestyle . MatA binds more weakly to pfliA and to pfliC, and their levels are equal to those observed for matB...

## Annotation

FUNCTION: Part of the ecpRABCDE operon, which encodes the E.coli common pilus (ECP). ECP is found in both commensal and pathogenic strains and plays a dual role in early-stage biofilm development and host cell recognition. Positively regulates the expression of the ecp operon (By similarity). Also represses expression of the flagellar master operon flhDC, and consequently prevents flagellum biosynthesis and motility. Acts by binding to the regulatory region of the flhDC operon (Probable). {ECO:0000250, ECO:0000269|PubMed:22422754, ECO:0000305}.

## Outgoing Edges (9)

- `activates` --> [[gene.b0293|gene.b0293]] `RegulonDB` `S` - regulator=MatA; target=ecpA; function=+
- `activates` --> [[gene.b0294|gene.b0294]] `RegulonDB` `S` - regulator=MatA; target=matA; function=+
- `represses` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=MatA; target=flhC; function=-
- `represses` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=MatA; target=flhD; function=-
- `represses` --> [[gene.b1920|gene.b1920]] `RegulonDB` `S` - regulator=MatA; target=tcyJ; function=-
- `represses` --> [[gene.b1921|gene.b1921]] `RegulonDB` `S` - regulator=MatA; target=fliZ; function=-
- `represses` --> [[gene.b1922|gene.b1922]] `RegulonDB` `S` - regulator=MatA; target=fliA; function=-
- `represses` --> [[gene.b1923|gene.b1923]] `RegulonDB` `S` - regulator=MatA; target=fliC; function=-
- `represses` --> [[gene.b4827|gene.b4827]] `RegulonDB` `S` - regulator=MatA; target=fliX; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b0294|gene.b0294]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P71301`
- `KEGG:ecj:JW5031;eco:b0294;`
- `GeneID:944966;`
- `GO:GO:0003677; GO:0005667; GO:0005737; GO:0006355; GO:1902021`

## Notes

HTH-type transcriptional regulator EcpR
