---
entity_id: "protein.P0ACH5"
entity_type: "protein"
name: "marA"
source_database: "UniProt"
source_id: "P0ACH5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "marA b1531 JW5249"
---

# marA

`protein.P0ACH5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACH5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: May be a transcriptional activator of genes involved in the multiple antibiotic resistance (Mar) phenotype. It can also activate genes such as sodA, zwf and micF. MarA, "multiple antibiotic resistance" , participates in controlling several genes involved in resistance to antibiotics , oxidative stress , organic solvents , heavy metals , xenobiotics compounds , lipopolysaccharide (LPS) biosynthesis , and cell wall remodelling . The antibiotic resistance associated with MarA appears to involve the acidification of the cytoplasm . MarA, SoxS, and Rob are paralogous transcriptional regulators that show 45% amino acid identity between them ; the crystal structures for Rob and MarA confirm this similarity between them. They activate a common set of genes, but the expression and activity of each one of these proteins are induced by different signals. Many genes are regulated by all three proteins; however, some genes are regulated only by one of them. The differential regulation of these genes might be caused by the degeneracy of their DNA-binding sites . These three monomer proteins bind to the same DNA site, a degenerate 19-bp sequence known as the sox-mar-rob box, which has to be in a specific orientation and distance relative to the -35 and -10 boxes of the promoter...

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

FUNCTION: May be a transcriptional activator of genes involved in the multiple antibiotic resistance (Mar) phenotype. It can also activate genes such as sodA, zwf and micF.

## Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Outgoing Edges (43)

- `activates` --> [[gene.b0096|gene.b0096]] `RegulonDB` `S` - regulator=MarA; target=lpxC; function=+
- `activates` --> [[gene.b0462|gene.b0462]] `RegulonDB` `S` - regulator=MarA; target=acrB; function=+
- `activates` --> [[gene.b0463|gene.b0463]] `RegulonDB` `S` - regulator=MarA; target=acrA; function=+
- `activates` --> [[gene.b0578|gene.b0578]] `RegulonDB` `S` - regulator=MarA; target=nfsB; function=+
- `activates` --> [[gene.b0850|gene.b0850]] `RegulonDB` `S` - regulator=MarA; target=ybjC; function=+
- `activates` --> [[gene.b0851|gene.b0851]] `RegulonDB` `S` - regulator=MarA; target=nfsA; function=+
- `activates` --> [[gene.b0852|gene.b0852]] `RegulonDB` `S` - regulator=MarA; target=rimK; function=+
- `activates` --> [[gene.b0853|gene.b0853]] `RegulonDB` `S` - regulator=MarA; target=ybjN; function=+
- `activates` --> [[gene.b0950|gene.b0950]] `RegulonDB` `S` - regulator=MarA; target=pqiA; function=+
- `activates` --> [[gene.b0951|gene.b0951]] `RegulonDB` `S` - regulator=MarA; target=pqiB; function=+
- `activates` --> [[gene.b0952|gene.b0952]] `RegulonDB` `S` - regulator=MarA; target=pqiC; function=+
- `activates` --> [[gene.b1054|gene.b1054]] `RegulonDB` `S` - regulator=MarA; target=lpxL; function=+
- `activates` --> [[gene.b1164|gene.b1164]] `RegulonDB` `C` - regulator=MarA; target=ycgZ; function=+
- `activates` --> [[gene.b1165|gene.b1165]] `RegulonDB` `C` - regulator=MarA; target=ymgA; function=+
- `activates` --> [[gene.b1166|gene.b1166]] `RegulonDB` `C` - regulator=MarA; target=ariR; function=+
- `activates` --> [[gene.b1167|gene.b1167]] `RegulonDB` `C` - regulator=MarA; target=ymgC; function=+
- `activates` --> [[gene.b1276|gene.b1276]] `RegulonDB` `S` - regulator=MarA; target=acnA; function=+
- `activates` --> [[gene.b1530|gene.b1530]] `RegulonDB` `C` - regulator=MarA; target=marR; function=+
- `activates` --> [[gene.b1531|gene.b1531]] `RegulonDB` `C` - regulator=MarA; target=marA; function=+
- `activates` --> [[gene.b1532|gene.b1532]] `RegulonDB` `C` - regulator=MarA; target=marB; function=+
- `activates` --> [[gene.b1611|gene.b1611]] `RegulonDB` `S` - regulator=MarA; target=fumC; function=+
- `activates` --> [[gene.b1852|gene.b1852]] `RegulonDB` `S` - regulator=MarA; target=zwf; function=+
- `activates` --> [[gene.b2237|gene.b2237]] `RegulonDB` `S` - regulator=MarA; target=inaA; function=+
- `activates` --> [[gene.b2509|gene.b2509]] `RegulonDB` `S` - regulator=MarA; target=xseA; function=+
- `activates` --> [[gene.b3191|gene.b3191]] `RegulonDB` `S` - regulator=MarA; target=mlaB; function=+
- `activates` --> [[gene.b3192|gene.b3192]] `RegulonDB` `S` - regulator=MarA; target=mlaC; function=+
- `activates` --> [[gene.b3193|gene.b3193]] `RegulonDB` `S` - regulator=MarA; target=mlaD; function=+
- `activates` --> [[gene.b3194|gene.b3194]] `RegulonDB` `S` - regulator=MarA; target=mlaE; function=+
- `activates` --> [[gene.b3195|gene.b3195]] `RegulonDB` `S` - regulator=MarA; target=mlaF; function=+
- `activates` --> [[gene.b3624|gene.b3624]] `RegulonDB` `S` - regulator=MarA; target=waaZ; function=+
- `activates` --> [[gene.b3625|gene.b3625]] `RegulonDB` `S` - regulator=MarA; target=waaY; function=+
- `activates` --> [[gene.b3908|gene.b3908]] `RegulonDB` `S` - regulator=MarA; target=sodA; function=+
- `activates` --> [[gene.b3924|gene.b3924]] `RegulonDB` `S` - regulator=MarA; target=fpr; function=+
- `activates` --> [[gene.b4439|gene.b4439]] `RegulonDB` `S` - regulator=MarA; target=micF; function=+
- `represses` --> [[gene.b0342|gene.b0342]] `RegulonDB` `C` - regulator=MarA; target=lacA; function=-
- `represses` --> [[gene.b0343|gene.b0343]] `RegulonDB` `C` - regulator=MarA; target=lacY; function=-
- `represses` --> [[gene.b0344|gene.b0344]] `RegulonDB` `C` - regulator=MarA; target=lacZ; function=-
- `represses` --> [[gene.b2134|gene.b2134]] `RegulonDB|EcoCyc` `S` - regulator=MarA; target=pbpG; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` --> [[gene.b3508|gene.b3508]] `RegulonDB` `S` - regulator=MarA; target=yhiD; function=-
- `represses` --> [[gene.b3509|gene.b3509]] `RegulonDB` `S` - regulator=MarA; target=hdeB; function=-
- `represses` --> [[gene.b3510|gene.b3510]] `RegulonDB` `S` - regulator=MarA; target=hdeA; function=-
- `represses` --> [[gene.b4177|gene.b4177]] `RegulonDB` `C` - regulator=MarA; target=purA; function=-
- `represses` --> [[gene.b4396|gene.b4396]] `RegulonDB` `C` - regulator=MarA; target=rob; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b1531|gene.b1531]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACH5`
- `KEGG:ecj:JW5249;eco:b1531;ecoc:C3026_08845;`
- `GeneID:93775695;947613;`
- `GO:GO:0001108; GO:0003677; GO:0003700; GO:0005829; GO:0006355; GO:0043565; GO:0045892; GO:0045893; GO:0046677`

## Notes

Multiple antibiotic resistance protein MarA
