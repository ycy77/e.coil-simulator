---
entity_id: "protein.P0ACI0"
entity_type: "protein"
name: "rob"
source_database: "UniProt"
source_id: "P0ACI0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rob b4396 JW4359"
---

# rob

`protein.P0ACI0`

## Static

- Type: `protein`
- Source: `UniProt:P0ACI0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator (By similarity). Binds to the right arm of the replication origin oriC of the chromosome (PubMed:8449900). Rob binding may influence the formation of the nucleoprotein structure, required for oriC function in the initiation of replication (PubMed:8449900). {ECO:0000250|UniProtKB:Q8ZJU7, ECO:0000269|PubMed:8449900}. Rob is a transcriptional dual regulator. Its N-terminal domain shares 49% identity with MarA and SoxS . These proteins activate a common set of about 50 target genes , the marA/soxS/rob regulon, which is involved in antibiotic resistance , superoxide resistance , and tolerance to organic solvents and heavy metals . Ciprofloxacin is one of the antibiotics against which Rob appears to be involved in resistance . Inhibition of rob expression by CRISPRi reduced cellular fitness under treatment with the antibiotics verapamil or carbonyl cyanide 3-chlorophenylhydrazone (CCCP) . The activity of each protein is induced by different signals: the activity of Rob is increased with dipyridyl, bile salts, or decanoate , and the activities of MarA and SoxS are increased by the aromatic weak acid salicylate and oxidative stress , respectively. Cross talk between the mar and rob systems plays an important role in the response to salicylate . Many genes are regulated by all three proteins; however, some genes are regulated by only one of them...

## Annotation

FUNCTION: Transcriptional regulator (By similarity). Binds to the right arm of the replication origin oriC of the chromosome (PubMed:8449900). Rob binding may influence the formation of the nucleoprotein structure, required for oriC function in the initiation of replication (PubMed:8449900). {ECO:0000250|UniProtKB:Q8ZJU7, ECO:0000269|PubMed:8449900}.

## Outgoing Edges (18)

- `activates` --> [[gene.b0462|gene.b0462]] `RegulonDB` `S` - regulator=Rob; target=acrB; function=+
- `activates` --> [[gene.b0463|gene.b0463]] `RegulonDB` `S` - regulator=Rob; target=acrA; function=+
- `activates` --> [[gene.b1224|gene.b1224]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b1530|gene.b1530]] `RegulonDB` `C` - regulator=Rob; target=marR; function=+
- `activates` --> [[gene.b1531|gene.b1531]] `RegulonDB` `C` - regulator=Rob; target=marA; function=+
- `activates` --> [[gene.b1532|gene.b1532]] `RegulonDB` `C` - regulator=Rob; target=marB; function=+
- `activates` --> [[gene.b1611|gene.b1611]] `RegulonDB` `S` - regulator=Rob; target=fumC; function=+
- `activates` --> [[gene.b1852|gene.b1852]] `RegulonDB` `S` - regulator=Rob; target=zwf; function=+
- `activates` --> [[gene.b2077|gene.b2077]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b2237|gene.b2237]] `RegulonDB` `S` - regulator=Rob; target=inaA; function=+
- `activates` --> [[gene.b3049|gene.b3049]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4439|gene.b4439]] `RegulonDB` `S` - regulator=Rob; target=micF; function=+
- `represses` --> [[gene.b1748|gene.b1748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b1805|gene.b1805]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4067|gene.b4067]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4068|gene.b4068]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4069|gene.b4069]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4396|gene.b4396]] `RegulonDB` `S` - regulator=Rob; target=rob; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4396|gene.b4396]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACI0`
- `KEGG:ecj:JW4359;eco:b4396;ecoc:C3026_23755;`
- `GeneID:93777449;948916;`
- `GO:GO:0001108; GO:0003700; GO:0005829; GO:0006355; GO:0043565`

## Notes

Right origin-binding protein
