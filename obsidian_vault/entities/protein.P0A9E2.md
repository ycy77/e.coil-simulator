---
entity_id: "protein.P0A9E2"
entity_type: "protein"
name: "soxS"
source_database: "UniProt"
source_id: "P0A9E2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "soxS b4062 JW4023"
---

# soxS

`protein.P0A9E2`

## Static

- Type: `protein`
- Source: `UniProt:P0A9E2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Transcriptional activator of the superoxide response regulon of E.coli that includes at least 10 genes such as sodA, nfo, zwf and micF. Binds the DNA sequence 5'-GCACN(7)CAA-3'. It also facilitates the subsequent binding of RNA polymerase to the micF and the nfo promoters. SoxS is a dual transcriptional activator and participates in the removal of superoxide and nitric oxide and protection from organic solvents and antibiotics . SoxS shares 49% identity with MarA and the N-terminal domain of Rob . These proteins activate a common set of about 50 target genes , the marA/soxS/rob regulon, involved in antibiotic resistance , superoxide resistance , and tolerance to organic solvents and heavy metals . The activity of each protein is induced by different signals: the activity of Rob is increased with dipyridyl, bile salts, or decanoate , and the activities of MarA and SoxS are increased by the aromatic weak acid salicylate and by oxidative stress , respectively. SoxS was induced by tellurite (TeO32-) in a DNA microarray analysis . Many genes are regulated by all three proteins; however, some genes are regulated by only one of them. The differential regulation of these genes might be caused by the degeneracy of their DNA-binding sites...

## Annotation

FUNCTION: Transcriptional activator of the superoxide response regulon of E.coli that includes at least 10 genes such as sodA, nfo, zwf and micF. Binds the DNA sequence 5'-GCACN(7)CAA-3'. It also facilitates the subsequent binding of RNA polymerase to the micF and the nfo promoters.

## Outgoing Edges (37)

- `activates` --> [[gene.b0447|gene.b0447]] `RegulonDB` `S` - regulator=SoxS; target=decR; function=+
- `activates` --> [[gene.b0462|gene.b0462]] `RegulonDB` `C` - regulator=SoxS; target=acrB; function=+
- `activates` --> [[gene.b0463|gene.b0463]] `RegulonDB` `C` - regulator=SoxS; target=acrA; function=+
- `activates` --> [[gene.b0578|gene.b0578]] `RegulonDB` `S` - regulator=SoxS; target=nfsB; function=+
- `activates` --> [[gene.b0683|gene.b0683]] `RegulonDB` `C` - regulator=SoxS; target=fur; function=+
- `activates` --> [[gene.b0684|gene.b0684]] `RegulonDB` `C` - regulator=SoxS; target=fldA; function=+
- `activates` --> [[gene.b0850|gene.b0850]] `RegulonDB` `C` - regulator=SoxS; target=ybjC; function=+
- `activates` --> [[gene.b0851|gene.b0851]] `RegulonDB` `C` - regulator=SoxS; target=nfsA; function=+
- `activates` --> [[gene.b0852|gene.b0852]] `RegulonDB` `S` - regulator=SoxS; target=rimK; function=+
- `activates` --> [[gene.b0853|gene.b0853]] `RegulonDB` `C` - regulator=SoxS; target=ybjN; function=+
- `activates` --> [[gene.b0950|gene.b0950]] `RegulonDB` `C` - regulator=SoxS; target=pqiA; function=+
- `activates` --> [[gene.b0951|gene.b0951]] `RegulonDB` `C` - regulator=SoxS; target=pqiB; function=+
- `activates` --> [[gene.b0952|gene.b0952]] `RegulonDB` `C` - regulator=SoxS; target=pqiC; function=+
- `activates` --> [[gene.b1101|gene.b1101]] `RegulonDB` `S` - regulator=SoxS; target=ptsG; function=+
- `activates` --> [[gene.b1276|gene.b1276]] `RegulonDB` `C` - regulator=SoxS; target=acnA; function=+
- `activates` --> [[gene.b1277|gene.b1277]] `RegulonDB` `C` - regulator=SoxS; target=ribA; function=+
- `activates` --> [[gene.b1377|gene.b1377]] `RegulonDB` `C` - regulator=SoxS; target=ompN; function=+
- `activates` --> [[gene.b1378|gene.b1378]] `RegulonDB` `C` - regulator=SoxS; target=ydbK; function=+
- `activates` --> [[gene.b1530|gene.b1530]] `RegulonDB` `S` - regulator=SoxS; target=marR; function=+
- `activates` --> [[gene.b1531|gene.b1531]] `RegulonDB` `S` - regulator=SoxS; target=marA; function=+
- `activates` --> [[gene.b1532|gene.b1532]] `RegulonDB` `S` - regulator=SoxS; target=marB; function=+
- `activates` --> [[gene.b1611|gene.b1611]] `RegulonDB` `C` - regulator=SoxS; target=fumC; function=+
- `activates` --> [[gene.b1852|gene.b1852]] `RegulonDB` `C` - regulator=SoxS; target=zwf; function=+
- `activates` --> [[gene.b2159|gene.b2159]] `RegulonDB` `S` - regulator=SoxS; target=nfo; function=+
- `activates` --> [[gene.b2237|gene.b2237]] `RegulonDB` `S` - regulator=SoxS; target=inaA; function=+
- `activates` --> [[gene.b3207|gene.b3207]] `RegulonDB` `S` - regulator=SoxS; target=yrbL; function=+
- `activates` --> [[gene.b3624|gene.b3624]] `RegulonDB` `S` - regulator=SoxS; target=waaZ; function=+
- `activates` --> [[gene.b3625|gene.b3625]] `RegulonDB` `S` - regulator=SoxS; target=waaY; function=+
- `activates` --> [[gene.b3662|gene.b3662]] `RegulonDB` `S` - regulator=SoxS; target=nepI; function=+
- `activates` --> [[gene.b3908|gene.b3908]] `RegulonDB` `C` - regulator=SoxS; target=sodA; function=+
- `activates` --> [[gene.b3924|gene.b3924]] `RegulonDB` `C` - regulator=SoxS; target=fpr; function=+
- `activates` --> [[gene.b4131|gene.b4131]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` --> [[gene.b4439|gene.b4439]] `RegulonDB` `C` - regulator=SoxS; target=micF; function=+
- `activates` --> [[gene.b4637|gene.b4637]] `RegulonDB` `C` - regulator=SoxS; target=uof; function=+
- `represses` --> [[gene.b2134|gene.b2134]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b4062|gene.b4062]] `RegulonDB` `C` - regulator=SoxS; target=soxS; function=-
- `represses` --> [[gene.b4396|gene.b4396]] `RegulonDB` `S` - regulator=SoxS; target=rob; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4062|gene.b4062]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9E2`
- `KEGG:ecj:JW4023;eco:b4062;ecoc:C3026_21950;`
- `GeneID:93777769;948567;`
- `GO:GO:0000987; GO:0001108; GO:0003700; GO:0005829; GO:0006355; GO:0043565`

## Notes

Regulatory protein SoxS
