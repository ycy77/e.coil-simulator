---
entity_id: "protein.P0ACJ8"
entity_type: "protein"
name: "crp"
source_database: "UniProt"
source_id: "P0ACJ8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "crp cap csm b3357 JW5702"
---

# crp

`protein.P0ACJ8`

## Static

- Type: `protein`
- Source: `UniProt:P0ACJ8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: A global transcription regulator, which plays a major role in carbon catabolite repression (CCR) as well as other processes. Binds cyclic AMP (cAMP) which allosterically activates DNA binding (to consensus sequence 5'-AAATGTGATCTAGATCACATTT-3') to directly regulate the transcription of about 300 genes in about 200 operons and indirectly regulate the expression of about half the genome. There are 3 classes of CRP promoters; class I promoters have a single CRP-binding site upstream of the RNA polymerase (RNAP)-binding site, whereas in class II promoters the single CRP- and RNAP-binding site overlap, CRP making multiple contacts with RNAP. Class III promoters require multiple activator molecules, including at least one CRP dimer. CRP can act as an activator, repressor, coactivator or corepressor. Induces a severe bend in DNA (about 87 degrees), bringing upstream promoter elements into contact with RNAP. Acts as a negative regulator of its own synthesis as well as for adenylate cyclase (cyaA), which generates cAMP. High levels of active CRP are detrimental to growth (PubMed:16260780). In CCR it prevents expression of genes involved in catabolism of nonpreferred carbon sources when glucose is present. CCR involves cAMP, adenylate cyclase (cyaA), CRP and the EIIA-Glc component of the PTS (crr)...

## Biological Role

Component of DNA-binding transcriptional repressor CRP-Sxy (complex.ecocyc.CPLX0-8312), DNA-binding transcriptional dual regulator CRP (complex.ecocyc.PC00004).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: A global transcription regulator, which plays a major role in carbon catabolite repression (CCR) as well as other processes. Binds cyclic AMP (cAMP) which allosterically activates DNA binding (to consensus sequence 5'-AAATGTGATCTAGATCACATTT-3') to directly regulate the transcription of about 300 genes in about 200 operons and indirectly regulate the expression of about half the genome. There are 3 classes of CRP promoters; class I promoters have a single CRP-binding site upstream of the RNA polymerase (RNAP)-binding site, whereas in class II promoters the single CRP- and RNAP-binding site overlap, CRP making multiple contacts with RNAP. Class III promoters require multiple activator molecules, including at least one CRP dimer. CRP can act as an activator, repressor, coactivator or corepressor. Induces a severe bend in DNA (about 87 degrees), bringing upstream promoter elements into contact with RNAP. Acts as a negative regulator of its own synthesis as well as for adenylate cyclase (cyaA), which generates cAMP. High levels of active CRP are detrimental to growth (PubMed:16260780). In CCR it prevents expression of genes involved in catabolism of nonpreferred carbon sources when glucose is present. CCR involves cAMP, adenylate cyclase (cyaA), CRP and the EIIA-Glc component of the PTS (crr). In the presence of glucose, EIIA-Glc is dephosphorylated, and does not activate adenylate cyclase, leading to reduced cAMP and thus decreased CRP activity. When glucose is absent cAMP binds to CRP, upregulating expression of genes involved in the consumption of non-glucose carbon sources. Also plays a role in many other processes (see PubMed:22573269). {ECO:0000269|PubMed:10860739, ECO:0000269|PubMed:10860740, ECO:0000269|PubMed:14990258, ECO:0000269|PubMed:15520470, ECO:0000269|PubMed:16260780, ECO:0000269|PubMed:16301522, ECO:0000269|PubMed:1646077, ECO:0000269|PubMed:2982847, ECO:0000269|PubMed:7966284, ECO:0000269|PubMed:8392187, ECO:0000269|PubMed:8978616}.; FUNCTION: Among the targets of CRP is the spf gene which encodes the dual-function sRNA Spot 42; spf expression is repressed by CRP (PubMed:2454912). Spot 42 base pairs with and represses expression from a number of mRNAs encoding proteins involved in the uptake and catabolism of nonpreferred carbon sources. CRP and Spot 42 coregulate at least 14 operons involved in cellular metabolism, forming a coherent feedforward loop (PubMed:21292161). Interaction with SpfP, encoded within the Spot 42 RNA, reinforces this feedforward loop (PubMed:35239441). {ECO:0000269|PubMed:21292161, ECO:0000269|PubMed:2454912, ECO:0000269|PubMed:35239441}.; FUNCTION: Some mutants (called CRP* or CAP*) are constitutively active even in the absence of cAMP (PubMed:19439203). Strain DHKD, a CAP* mutant, confers cAMP-independent expression and relief of catabolite repression of beta-galactosidase and tryptophanase synthesis (PubMed:14990258). Strain CA8404, another CAP* mutant, confers cAMP-independent expression and relief of catabolite repression of beta-galactosidase but not of tryptophanase synthesis (PubMed:14990258). {ECO:0000269|PubMed:14990258, ECO:0000303|PubMed:19439203}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02024` Quorum sensing (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (381)

- `activates` --> [[gene.b0035|gene.b0035]] `RegulonDB` `S` - regulator=CRP; target=caiE; function=+
- `activates` --> [[gene.b0036|gene.b0036]] `RegulonDB` `S` - regulator=CRP; target=caiD; function=+
- `activates` --> [[gene.b0037|gene.b0037]] `RegulonDB` `S` - regulator=CRP; target=caiC; function=+
- `activates` --> [[gene.b0038|gene.b0038]] `RegulonDB` `S` - regulator=CRP; target=caiB; function=+
- `activates` --> [[gene.b0039|gene.b0039]] `RegulonDB` `S` - regulator=CRP; target=caiA; function=+
- `activates` --> [[gene.b0040|gene.b0040]] `RegulonDB` `S` - regulator=CRP; target=caiT; function=+
- `activates` --> [[gene.b0061|gene.b0061]] `RegulonDB` `C` - regulator=CRP; target=araD; function=+
- `activates` --> [[gene.b0062|gene.b0062]] `RegulonDB` `C` - regulator=CRP; target=araA; function=+
- `activates` --> [[gene.b0063|gene.b0063]] `RegulonDB` `C` - regulator=CRP; target=araB; function=+
- `activates` --> [[gene.b0064|gene.b0064]] `RegulonDB` `C` - regulator=CRP; target=araC; function=+
- `activates` --> [[gene.b0106|gene.b0106]] `RegulonDB` `S` - regulator=CRP; target=hofC; function=+
- `activates` --> [[gene.b0107|gene.b0107]] `RegulonDB` `S` - regulator=CRP; target=hofB; function=+
- `activates` --> [[gene.b0108|gene.b0108]] `RegulonDB` `S` - regulator=CRP; target=ppdD; function=+
- `activates` --> [[gene.b0125|gene.b0125]] `RegulonDB` `C` - regulator=CRP; target=hpt; function=+
- `activates` --> [[gene.b0328|gene.b0328]] `RegulonDB` `S` - regulator=CRP; target=yahN; function=+
- `activates` --> [[gene.b0330|gene.b0330]] `RegulonDB` `C` - regulator=CRP; target=prpR; function=+
- `activates` --> [[gene.b0331|gene.b0331]] `RegulonDB` `C` - regulator=CRP; target=prpB; function=+
- `activates` --> [[gene.b0333|gene.b0333]] `RegulonDB` `C` - regulator=CRP; target=prpC; function=+
- `activates` --> [[gene.b0334|gene.b0334]] `RegulonDB` `C` - regulator=CRP; target=prpD; function=+
- `activates` --> [[gene.b0335|gene.b0335]] `RegulonDB` `C` - regulator=CRP; target=prpE; function=+
- `activates` --> [[gene.b0342|gene.b0342]] `RegulonDB` `C` - regulator=CRP; target=lacA; function=-+
- `activates` --> [[gene.b0343|gene.b0343]] `RegulonDB` `S` - regulator=CRP; target=lacY; function=-+
- `activates` --> [[gene.b0344|gene.b0344]] `RegulonDB` `C` - regulator=CRP; target=lacZ; function=-+
- `activates` --> [[gene.b0345|gene.b0345]] `RegulonDB` `S` - regulator=CRP; target=lacI; function=+
- `activates` --> [[gene.b0346|gene.b0346]] `RegulonDB` `S` - regulator=CRP; target=mhpR; function=+
- `activates` --> [[gene.b0347|gene.b0347]] `RegulonDB` `S` - regulator=CRP; target=mhpA; function=+
- `activates` --> [[gene.b0348|gene.b0348]] `RegulonDB` `S` - regulator=CRP; target=mhpB; function=+
- `activates` --> [[gene.b0349|gene.b0349]] `RegulonDB` `S` - regulator=CRP; target=mhpC; function=+
- `activates` --> [[gene.b0350|gene.b0350]] `RegulonDB` `S` - regulator=CRP; target=mhpD; function=+
- `activates` --> [[gene.b0351|gene.b0351]] `RegulonDB` `S` - regulator=CRP; target=mhpF; function=+
- `activates` --> [[gene.b0352|gene.b0352]] `RegulonDB` `S` - regulator=CRP; target=mhpE; function=+
- `activates` --> [[gene.b0396|gene.b0396]] `RegulonDB` `S` - regulator=CRP; target=araJ; function=-+
- `activates` --> [[gene.b0411|gene.b0411]] `RegulonDB` `C` - regulator=CRP; target=tsx; function=-+
- `activates` --> [[gene.b0440|gene.b0440]] `RegulonDB` `S` - regulator=CRP; target=hupB; function=+
- `activates` --> [[gene.b0598|gene.b0598]] `RegulonDB` `S` - regulator=CRP; target=cstA; function=+
- `activates` --> [[gene.b0623|gene.b0623]] `RegulonDB` `C` - regulator=CRP; target=cspE; function=+
- `activates` --> [[gene.b0651|gene.b0651]] `RegulonDB` `S` - regulator=CRP; target=rihA; function=+
- `activates` --> [[gene.b0675|gene.b0675]] `RegulonDB` `S` - regulator=CRP; target=umpH; function=-+
- `activates` --> [[gene.b0676|gene.b0676]] `RegulonDB` `S` - regulator=CRP; target=nagC; function=-+
- `activates` --> [[gene.b0677|gene.b0677]] `RegulonDB` `S` - regulator=CRP; target=nagA; function=-+
- `activates` --> [[gene.b0678|gene.b0678]] `RegulonDB` `S` - regulator=CRP; target=nagB; function=-+
- `activates` --> [[gene.b0679|gene.b0679]] `RegulonDB` `C` - regulator=CRP; target=nagE; function=-+
- `activates` --> [[gene.b0683|gene.b0683]] `RegulonDB` `S` - regulator=CRP; target=fur; function=+
- `activates` --> [[gene.b0720|gene.b0720]] `RegulonDB` `S` - regulator=CRP; target=gltA; function=+
- `activates` --> [[gene.b0721|gene.b0721]] `RegulonDB` `S` - regulator=CRP; target=sdhC; function=+
- `activates` --> [[gene.b0722|gene.b0722]] `RegulonDB` `S` - regulator=CRP; target=sdhD; function=+
- `activates` --> [[gene.b0723|gene.b0723]] `RegulonDB` `S` - regulator=CRP; target=sdhA; function=+
- `activates` --> [[gene.b0726|gene.b0726]] `RegulonDB` `S` - regulator=CRP; target=sucA; function=+
- `activates` --> [[gene.b0727|gene.b0727]] `RegulonDB` `S` - regulator=CRP; target=sucB; function=+
- `activates` --> [[gene.b0728|gene.b0728]] `RegulonDB` `S` - regulator=CRP; target=sucC; function=+
- `activates` --> [[gene.b0729|gene.b0729]] `RegulonDB` `S` - regulator=CRP; target=sucD; function=+
- `activates` --> [[gene.b0756|gene.b0756]] `RegulonDB` `S` - regulator=CRP; target=galM; function=-+
- `activates` --> [[gene.b0757|gene.b0757]] `RegulonDB` `S` - regulator=CRP; target=galK; function=-+
- `activates` --> [[gene.b0758|gene.b0758]] `RegulonDB` `S` - regulator=CRP; target=galT; function=-+
- `activates` --> [[gene.b0759|gene.b0759]] `RegulonDB` `S` - regulator=CRP; target=galE; function=-+
- `activates` --> [[gene.b0880|gene.b0880]] `RegulonDB` `C` - regulator=CRP; target=cspD; function=+
- `activates` --> [[gene.b0903|gene.b0903]] `RegulonDB` `C` - regulator=CRP; target=pflB; function=+
- `activates` --> [[gene.b0904|gene.b0904]] `RegulonDB` `C` - regulator=CRP; target=focA; function=+
- `activates` --> [[gene.b0953|gene.b0953]] `RegulonDB` `S` - regulator=CRP; target=rmf; function=+
- `activates` --> [[gene.b1101|gene.b1101]] `RegulonDB` `S` - regulator=CRP; target=ptsG; function=+
- `activates` --> [[gene.b1182|gene.b1182]] `RegulonDB` `C` - regulator=CRP; target=hlyE; function=+
- `activates` --> [[gene.b1189|gene.b1189]] `RegulonDB` `S` - regulator=CRP; target=dadA; function=-+
- `activates` --> [[gene.b1190|gene.b1190]] `RegulonDB` `S` - regulator=CRP; target=dadX; function=-+
- `activates` --> [[gene.b1205|gene.b1205]] `RegulonDB` `C` - regulator=CRP; target=ychH; function=+
- `activates` --> [[gene.b1339|gene.b1339]] `RegulonDB` `S` - regulator=CRP; target=abgR; function=+
- `activates` --> [[gene.b1387|gene.b1387]] `RegulonDB` `C` - regulator=CRP; target=paaZ; function=+
- `activates` --> [[gene.b1388|gene.b1388]] `RegulonDB` `C` - regulator=CRP; target=paaA; function=+
- `activates` --> [[gene.b1389|gene.b1389]] `RegulonDB` `C` - regulator=CRP; target=paaB; function=+
- `activates` --> [[gene.b1390|gene.b1390]] `RegulonDB` `C` - regulator=CRP; target=paaC; function=+
- `activates` --> [[gene.b1391|gene.b1391]] `RegulonDB` `C` - regulator=CRP; target=paaD; function=+
- `activates` --> [[gene.b1392|gene.b1392]] `RegulonDB` `C` - regulator=CRP; target=paaE; function=+
- `activates` --> [[gene.b1393|gene.b1393]] `RegulonDB` `C` - regulator=CRP; target=paaF; function=+
- `activates` --> [[gene.b1394|gene.b1394]] `RegulonDB` `C` - regulator=CRP; target=paaG; function=+
- `activates` --> [[gene.b1395|gene.b1395]] `RegulonDB` `C` - regulator=CRP; target=paaH; function=+
- `activates` --> [[gene.b1396|gene.b1396]] `RegulonDB` `C` - regulator=CRP; target=paaI; function=+
- `activates` --> [[gene.b1397|gene.b1397]] `RegulonDB` `C` - regulator=CRP; target=paaJ; function=+
- `activates` --> [[gene.b1398|gene.b1398]] `RegulonDB` `C` - regulator=CRP; target=paaK; function=+
- `activates` --> [[gene.b1420|gene.b1420]] `RegulonDB` `S` - regulator=CRP; target=mokB; function=+
- `activates` --> [[gene.b1421|gene.b1421]] `RegulonDB` `S` - regulator=CRP; target=trg; function=+
- `activates` --> [[gene.b1511|gene.b1511]] `RegulonDB` `C` - regulator=CRP; target=lsrK; function=+
- `activates` --> [[gene.b1512|gene.b1512]] `RegulonDB` `C` - regulator=CRP; target=lsrR; function=+
- `activates` --> [[gene.b1513|gene.b1513]] `RegulonDB` `C` - regulator=CRP; target=lsrA; function=+
- `activates` --> [[gene.b1514|gene.b1514]] `RegulonDB` `C` - regulator=CRP; target=lsrC; function=+
- `activates` --> [[gene.b1515|gene.b1515]] `RegulonDB` `C` - regulator=CRP; target=lsrD; function=+
- `activates` --> [[gene.b1516|gene.b1516]] `RegulonDB` `C` - regulator=CRP; target=lsrB; function=+
- `activates` --> [[gene.b1517|gene.b1517]] `RegulonDB` `C` - regulator=CRP; target=lsrF; function=+
- `activates` --> [[gene.b1518|gene.b1518]] `RegulonDB` `C` - regulator=CRP; target=lsrG; function=+
- `activates` --> [[gene.b1519|gene.b1519]] `RegulonDB` `C` - regulator=CRP; target=tam; function=+
- `activates` --> [[gene.b1580|gene.b1580]] `RegulonDB` `S` - regulator=CRP; target=rspB; function=+
- `activates` --> [[gene.b1581|gene.b1581]] `RegulonDB` `S` - regulator=CRP; target=rspA; function=+
- `activates` --> [[gene.b1620|gene.b1620]] `RegulonDB` `C` - regulator=CRP; target=malI; function=-+
- `activates` --> [[gene.b1621|gene.b1621]] `RegulonDB` `C` - regulator=CRP; target=malX; function=+
- `activates` --> [[gene.b1622|gene.b1622]] `RegulonDB` `C` - regulator=CRP; target=malY; function=+
- `activates` --> [[gene.b1733|gene.b1733]] `RegulonDB` `S` - regulator=CRP; target=chbG; function=+
- `activates` --> [[gene.b1734|gene.b1734]] `RegulonDB` `S` - regulator=CRP; target=chbF; function=+
- `activates` --> [[gene.b1735|gene.b1735]] `RegulonDB` `S` - regulator=CRP; target=chbR; function=+
- `activates` --> [[gene.b1736|gene.b1736]] `RegulonDB` `S` - regulator=CRP; target=chbA; function=+
- `activates` --> [[gene.b1737|gene.b1737]] `RegulonDB` `S` - regulator=CRP; target=chbC; function=+
- `activates` --> [[gene.b1738|gene.b1738]] `RegulonDB` `S` - regulator=CRP; target=chbB; function=+
- `activates` --> [[gene.b1805|gene.b1805]] `RegulonDB` `S` - regulator=CRP; target=fadD; function=+
- `activates` --> [[gene.b1819|gene.b1819]] `RegulonDB` `S` - regulator=CRP; target=manZ; function=+
- `activates` --> [[gene.b1891|gene.b1891]] `RegulonDB` `S` - regulator=CRP; target=flhC; function=+
- `activates` --> [[gene.b1892|gene.b1892]] `RegulonDB` `S` - regulator=CRP; target=flhD; function=+
- `activates` --> [[gene.b1900|gene.b1900]] `RegulonDB` `C` - regulator=CRP; target=araG; function=+
- `activates` --> [[gene.b1901|gene.b1901]] `RegulonDB` `C` - regulator=CRP; target=araF; function=+
- `activates` --> [[gene.b2009|gene.b2009]] `RegulonDB` `S` - regulator=CRP; target=sbmC; function=+
- `activates` --> [[gene.b2091|gene.b2091]] `RegulonDB` `C` - regulator=CRP; target=gatD; function=+
- `activates` --> [[gene.b2093|gene.b2093]] `RegulonDB` `C` - regulator=CRP; target=gatB; function=+
- `activates` --> [[gene.b2094|gene.b2094]] `RegulonDB` `C` - regulator=CRP; target=gatA; function=+
- `activates` --> [[gene.b2095|gene.b2095]] `RegulonDB` `C` - regulator=CRP; target=gatZ; function=+
- `activates` --> [[gene.b2096|gene.b2096]] `RegulonDB` `C` - regulator=CRP; target=gatY; function=+
- `activates` --> [[gene.b2143|gene.b2143]] `RegulonDB` `C` - regulator=CRP; target=cdd; function=-+
- `activates` --> [[gene.b2148|gene.b2148]] `RegulonDB` `C` - regulator=CRP; target=mglC; function=+
- `activates` --> [[gene.b2149|gene.b2149]] `RegulonDB` `C` - regulator=CRP; target=mglA; function=+
- `activates` --> [[gene.b2150|gene.b2150]] `RegulonDB` `C` - regulator=CRP; target=mglB; function=+
- `activates` --> [[gene.b2151|gene.b2151]] `RegulonDB` `S` - regulator=CRP; target=galS; function=+
- `activates` --> [[gene.b2165|gene.b2165]] `RegulonDB` `S` - regulator=CRP; target=psuG; function=+
- `activates` --> [[gene.b2166|gene.b2166]] `RegulonDB` `S` - regulator=CRP; target=psuK; function=+
- `activates` --> [[gene.b2239|gene.b2239]] `RegulonDB` `S` - regulator=CRP; target=glpQ; function=+
- `activates` --> [[gene.b2240|gene.b2240]] `RegulonDB` `S` - regulator=CRP; target=glpT; function=+
- `activates` --> [[gene.b2241|gene.b2241]] `RegulonDB` `S` - regulator=CRP; target=glpA; function=+
- `activates` --> [[gene.b2242|gene.b2242]] `RegulonDB` `S` - regulator=CRP; target=glpB; function=+
- `activates` --> [[gene.b2243|gene.b2243]] `RegulonDB` `S` - regulator=CRP; target=glpC; function=+
- `activates` --> [[gene.b2344|gene.b2344]] `RegulonDB` `S` - regulator=CRP; target=fadL; function=+
- `activates` --> [[gene.b2415|gene.b2415]] `RegulonDB` `S` - regulator=CRP; target=ptsH; function=-+
- `activates` --> [[gene.b2416|gene.b2416]] `RegulonDB` `S` - regulator=CRP; target=ptsI; function=-+
- `activates` --> [[gene.b2417|gene.b2417]] `RegulonDB` `S` - regulator=CRP; target=crr; function=-+
- `activates` --> [[gene.b2428|gene.b2428]] `RegulonDB` `S` - regulator=CRP; target=murQ; function=+
- `activates` --> [[gene.b2429|gene.b2429]] `RegulonDB` `S` - regulator=CRP; target=murP; function=+
- `activates` --> [[gene.b2507|gene.b2507]] `RegulonDB` `C` - regulator=CRP; target=guaA; function=+
- `activates` --> [[gene.b2508|gene.b2508]] `RegulonDB` `C` - regulator=CRP; target=guaB; function=+
- `activates` --> [[gene.b2570|gene.b2570]] `RegulonDB` `S` - regulator=CRP; target=rseC; function=+
- `activates` --> [[gene.b2571|gene.b2571]] `RegulonDB` `S` - regulator=CRP; target=rseB; function=+
- `activates` --> [[gene.b2572|gene.b2572]] `RegulonDB` `S` - regulator=CRP; target=rseA; function=+
- `activates` --> [[gene.b2573|gene.b2573]] `RegulonDB` `S` - regulator=CRP; target=rpoE; function=+
- `activates` --> [[gene.b2597|gene.b2597]] `RegulonDB` `S` - regulator=CRP; target=raiA; function=+
- `activates` --> [[gene.b2659|gene.b2659]] `RegulonDB` `S` - regulator=CRP; target=glaH; function=+
- `activates` --> [[gene.b2660|gene.b2660]] `RegulonDB` `S` - regulator=CRP; target=lhgD; function=+
- `activates` --> [[gene.b2661|gene.b2661]] `RegulonDB` `S` - regulator=CRP; target=gabD; function=+
- `activates` --> [[gene.b2662|gene.b2662]] `RegulonDB` `S` - regulator=CRP; target=gabT; function=+
- `activates` --> [[gene.b2663|gene.b2663]] `RegulonDB` `S` - regulator=CRP; target=gabP; function=+
- `activates` --> [[gene.b2715|gene.b2715]] `RegulonDB` `S` - regulator=CRP; target=ascF; function=+
- `activates` --> [[gene.b2716|gene.b2716]] `RegulonDB` `S` - regulator=CRP; target=ascB; function=+
- `activates` --> [[gene.b2761|gene.b2761]] `RegulonDB` `C` - regulator=CRP; target=cas3; function=+
- `activates` --> [[gene.b2774|gene.b2774]] `RegulonDB` `S` - regulator=CRP; target=ygcW; function=+
- `activates` --> [[gene.b2782|gene.b2782]] `RegulonDB` `C` - regulator=CRP; target=mazF; function=+
- `activates` --> [[gene.b2783|gene.b2783]] `RegulonDB` `C` - regulator=CRP; target=mazE; function=+
- `activates` --> [[gene.b2784|gene.b2784]] `RegulonDB` `C` - regulator=CRP; target=relA; function=+
- `activates` --> [[gene.b2799|gene.b2799]] `RegulonDB` `S` - regulator=CRP; target=fucO; function=+
- `activates` --> [[gene.b2800|gene.b2800]] `RegulonDB` `S` - regulator=CRP; target=fucA; function=+
- `activates` --> [[gene.b2801|gene.b2801]] `RegulonDB` `C` - regulator=CRP; target=fucP; function=+
- `activates` --> [[gene.b2802|gene.b2802]] `RegulonDB` `C` - regulator=CRP; target=fucI; function=+
- `activates` --> [[gene.b2803|gene.b2803]] `RegulonDB` `S` - regulator=CRP; target=fucK; function=+
- `activates` --> [[gene.b2804|gene.b2804]] `RegulonDB` `C` - regulator=CRP; target=fucU; function=+
- `activates` --> [[gene.b2805|gene.b2805]] `RegulonDB` `S` - regulator=CRP; target=fucR; function=+
- `activates` --> [[gene.b2840|gene.b2840]] `RegulonDB` `S` - regulator=CRP; target=ygeA; function=+
- `activates` --> [[gene.b2841|gene.b2841]] `RegulonDB` `S` - regulator=CRP; target=araE; function=+
- `activates` --> [[gene.b2844|gene.b2844]] `RegulonDB` `S` - regulator=CRP; target=yqeF; function=+
- `activates` --> [[gene.b2870|gene.b2870]] `RegulonDB` `S` - regulator=CRP; target=ygeW; function=+
- `activates` --> [[gene.b2903|gene.b2903]] `RegulonDB` `C` - regulator=CRP; target=gcvP; function=+
- `activates` --> [[gene.b2904|gene.b2904]] `RegulonDB` `C` - regulator=CRP; target=gcvH; function=+
- `activates` --> [[gene.b2905|gene.b2905]] `RegulonDB` `C` - regulator=CRP; target=gcvT; function=+
- `activates` --> [[gene.b2925|gene.b2925]] `RegulonDB` `C` - regulator=CRP; target=fbaA; function=+
- `activates` --> [[gene.b2926|gene.b2926]] `RegulonDB` `C` - regulator=CRP; target=pgk; function=+
- `activates` --> [[gene.b2927|gene.b2927]] `RegulonDB` `C` - regulator=CRP; target=epd; function=+
- `activates` --> [[gene.b2957|gene.b2957]] `RegulonDB` `S` - regulator=CRP; target=ansB; function=+
- `activates` --> [[gene.b2964|gene.b2964]] `RegulonDB` `C` - regulator=CRP; target=nupG; function=-+
- `activates` --> [[gene.b3072|gene.b3072]] `RegulonDB` `C` - regulator=CRP; target=aer; function=+
- `activates` --> [[gene.b3113|gene.b3113]] `RegulonDB` `C` - regulator=CRP; target=tdcF; function=+
- `activates` --> [[gene.b3114|gene.b3114]] `RegulonDB` `C` - regulator=CRP; target=tdcE; function=+
- `activates` --> [[gene.b3115|gene.b3115]] `RegulonDB` `C` - regulator=CRP; target=tdcD; function=+
- `activates` --> [[gene.b3116|gene.b3116]] `RegulonDB` `C` - regulator=CRP; target=tdcC; function=+
- `activates` --> [[gene.b3117|gene.b3117]] `RegulonDB` `C` - regulator=CRP; target=tdcB; function=+
- `activates` --> [[gene.b3118|gene.b3118]] `RegulonDB` `C` - regulator=CRP; target=tdcA; function=+
- `activates` --> [[gene.b3132|gene.b3132]] `RegulonDB` `S` - regulator=CRP; target=kbaZ; function=+
- `activates` --> [[gene.b3133|gene.b3133]] `RegulonDB` `S` - regulator=CRP; target=agaV; function=+
- `activates` --> [[gene.b3172|gene.b3172]] `RegulonDB` `C` - regulator=CRP; target=argG; function=+
- `activates` --> [[gene.b3221|gene.b3221]] `RegulonDB` `S` - regulator=CRP; target=nanQ; function=+
- `activates` --> [[gene.b3222|gene.b3222]] `RegulonDB` `S` - regulator=CRP; target=nanK; function=+
- `activates` --> [[gene.b3223|gene.b3223]] `RegulonDB` `S` - regulator=CRP; target=nanE; function=+
- `activates` --> [[gene.b3224|gene.b3224]] `RegulonDB` `S` - regulator=CRP; target=nanT; function=+
- `activates` --> [[gene.b3225|gene.b3225]] `RegulonDB` `S` - regulator=CRP; target=nanA; function=+
- `activates` --> [[gene.b3356|gene.b3356]] `RegulonDB` `C` - regulator=CRP; target=yhfA; function=-+
- `activates` --> [[gene.b3357|gene.b3357]] `RegulonDB` `C` - regulator=CRP; target=crp; function=-+
- `activates` --> [[gene.b3363|gene.b3363]] `RegulonDB` `S` - regulator=CRP; target=ppiA; function=-+
- `activates` --> [[gene.b3392|gene.b3392]] `RegulonDB` `S` - regulator=CRP; target=hofP; function=+
- `activates` --> [[gene.b3393|gene.b3393]] `RegulonDB` `S` - regulator=CRP; target=hofO; function=+
- `activates` --> [[gene.b3394|gene.b3394]] `RegulonDB` `S` - regulator=CRP; target=hofN; function=+
- `activates` --> [[gene.b3395|gene.b3395]] `RegulonDB` `S` - regulator=CRP; target=hofM; function=+
- `activates` --> [[gene.b3403|gene.b3403]] `RegulonDB` `S` - regulator=CRP; target=pck; function=-+
- `activates` --> [[gene.b3404|gene.b3404]] `RegulonDB` `C` - regulator=CRP; target=envZ; function=-+
- `activates` --> [[gene.b3405|gene.b3405]] `RegulonDB` `C` - regulator=CRP; target=ompR; function=-+
- `activates` --> [[gene.b3415|gene.b3415]] `RegulonDB` `C` - regulator=CRP; target=gntT; function=+
- `activates` --> [[gene.b3418|gene.b3418]] `RegulonDB` `S` - regulator=CRP; target=malT; function=+
- `activates` --> [[gene.b3424|gene.b3424]] `RegulonDB` `S` - regulator=CRP; target=glpG; function=+
- `activates` --> [[gene.b3425|gene.b3425]] `RegulonDB` `S` - regulator=CRP; target=glpE; function=+
- `activates` --> [[gene.b3426|gene.b3426]] `RegulonDB` `S` - regulator=CRP; target=glpD; function=+
- `activates` --> [[gene.b3428|gene.b3428]] `RegulonDB` `S` - regulator=CRP; target=glgP; function=+
- `activates` --> [[gene.b3429|gene.b3429]] `RegulonDB` `S` - regulator=CRP; target=glgA; function=+
- `activates` --> [[gene.b3430|gene.b3430]] `RegulonDB` `S` - regulator=CRP; target=glgC; function=+
- `activates` --> [[gene.b3437|gene.b3437]] `RegulonDB` `S` - regulator=CRP; target=gntK; function=+
- `activates` --> [[gene.b3449|gene.b3449]] `RegulonDB` `S` - regulator=CRP; target=ugpQ; function=+
- `activates` --> [[gene.b3450|gene.b3450]] `RegulonDB` `S` - regulator=CRP; target=ugpC; function=+
- `activates` --> [[gene.b3451|gene.b3451]] `RegulonDB` `S` - regulator=CRP; target=ugpE; function=+
- `activates` --> [[gene.b3452|gene.b3452]] `RegulonDB` `S` - regulator=CRP; target=ugpA; function=+
- `activates` --> [[gene.b3453|gene.b3453]] `RegulonDB` `S` - regulator=CRP; target=ugpB; function=+
- `activates` --> [[gene.b3461|gene.b3461]] `RegulonDB` `S` - regulator=CRP; target=rpoH; function=-+
- `activates` --> [[gene.b3528|gene.b3528]] `RegulonDB` `S` - regulator=CRP; target=dctA; function=+
- `activates` --> [[gene.b3575|gene.b3575]] `RegulonDB` `S` - regulator=CRP; target=yiaK; function=+
- `activates` --> [[gene.b3576|gene.b3576]] `RegulonDB` `S` - regulator=CRP; target=yiaL; function=+
- `activates` --> [[gene.b3577|gene.b3577]] `RegulonDB` `S` - regulator=CRP; target=yiaM; function=+
- `activates` --> [[gene.b3578|gene.b3578]] `RegulonDB` `S` - regulator=CRP; target=yiaN; function=+
- `activates` --> [[gene.b3579|gene.b3579]] `RegulonDB` `S` - regulator=CRP; target=yiaO; function=+
- `activates` --> [[gene.b3580|gene.b3580]] `RegulonDB` `S` - regulator=CRP; target=lyxK; function=+
- `activates` --> [[gene.b3581|gene.b3581]] `RegulonDB` `S` - regulator=CRP; target=sgbH; function=+
- `activates` --> [[gene.b3582|gene.b3582]] `RegulonDB` `S` - regulator=CRP; target=sgbU; function=+
- `activates` --> [[gene.b3583|gene.b3583]] `RegulonDB` `S` - regulator=CRP; target=sgbE; function=+
- `activates` --> [[gene.b3588|gene.b3588]] `RegulonDB` `S` - regulator=CRP; target=aldB; function=+
- `activates` --> [[gene.b3599|gene.b3599]] `RegulonDB` `S` - regulator=CRP; target=mtlA; function=+
- `activates` --> [[gene.b3600|gene.b3600]] `RegulonDB` `S` - regulator=CRP; target=mtlD; function=+
- `activates` --> [[gene.b3601|gene.b3601]] `RegulonDB` `S` - regulator=CRP; target=mtlR; function=+
- `activates` --> [[gene.b3608|gene.b3608]] `RegulonDB` `C` - regulator=CRP; target=gpsA; function=+
- `activates` --> [[gene.b3609|gene.b3609]] `RegulonDB` `C` - regulator=CRP; target=secB; function=+
- `activates` --> [[gene.b3666|gene.b3666]] `RegulonDB` `C` - regulator=CRP; target=uhpT; function=+
- `activates` --> [[gene.b3670|gene.b3670]] `RegulonDB` `S` - regulator=CRP; target=ilvN; function=+
- `activates` --> [[gene.b3671|gene.b3671]] `RegulonDB` `S` - regulator=CRP; target=ilvB; function=+
- `activates` --> [[gene.b3672|gene.b3672]] `RegulonDB` `S` - regulator=CRP; target=ivbL; function=+
- `activates` --> [[gene.b3691|gene.b3691]] `RegulonDB` `C` - regulator=CRP; target=dgoT; function=+
- `activates` --> [[gene.b3693|gene.b3693]] `RegulonDB` `C` - regulator=CRP; target=dgoK; function=+
- `activates` --> [[gene.b3707|gene.b3707]] `RegulonDB` `S` - regulator=CRP; target=tnaC; function=+
- `activates` --> [[gene.b3708|gene.b3708]] `RegulonDB` `S` - regulator=CRP; target=tnaA; function=+
- `activates` --> [[gene.b3709|gene.b3709]] `RegulonDB` `S` - regulator=CRP; target=tnaB; function=+
- `activates` --> [[gene.b3721|gene.b3721]] `RegulonDB` `C` - regulator=CRP; target=bglB; function=+
- `activates` --> [[gene.b3722|gene.b3722]] `RegulonDB` `C` - regulator=CRP; target=bglF; function=+
- `activates` --> [[gene.b3723|gene.b3723]] `RegulonDB` `C` - regulator=CRP; target=bglG; function=+
- `activates` --> [[gene.b3831|gene.b3831]] `RegulonDB` `C` - regulator=CRP; target=udp; function=-+
- `activates` --> [[gene.b3884|gene.b3884]] `RegulonDB` `S` - regulator=CRP; target=csqR; function=-+
- `activates` --> [[gene.b3903|gene.b3903]] `RegulonDB` `S` - regulator=CRP; target=rhaA; function=+
- `activates` --> [[gene.b3904|gene.b3904]] `RegulonDB` `S` - regulator=CRP; target=rhaB; function=+
- `activates` --> [[gene.b3905|gene.b3905]] `RegulonDB` `C` - regulator=CRP; target=rhaS; function=+
- `activates` --> [[gene.b3906|gene.b3906]] `RegulonDB` `C` - regulator=CRP; target=rhaR; function=+
- `activates` --> [[gene.b3934|gene.b3934]] `RegulonDB` `S` - regulator=CRP; target=cytR; function=-+
- `activates` --> [[gene.b4000|gene.b4000]] `RegulonDB` `S` - regulator=CRP; target=hupA; function=+
- `activates` --> [[gene.b4031|gene.b4031]] `RegulonDB` `C` - regulator=CRP; target=xylE; function=+
- `activates` --> [[gene.b4032|gene.b4032]] `RegulonDB` `C` - regulator=CRP; target=malG; function=+
- `activates` --> [[gene.b4033|gene.b4033]] `RegulonDB` `C` - regulator=CRP; target=malF; function=+
- `activates` --> [[gene.b4034|gene.b4034]] `RegulonDB` `C` - regulator=CRP; target=malE; function=+
- `activates` --> [[gene.b4035|gene.b4035]] `RegulonDB` `C` - regulator=CRP; target=malK; function=+
- `activates` --> [[gene.b4036|gene.b4036]] `RegulonDB` `C` - regulator=CRP; target=lamB; function=+
- `activates` --> [[gene.b4037|gene.b4037]] `RegulonDB` `C` - regulator=CRP; target=malM; function=+
- `activates` --> [[gene.b4067|gene.b4067]] `RegulonDB` `C` - regulator=CRP; target=actP; function=+
- `activates` --> [[gene.b4068|gene.b4068]] `RegulonDB` `C` - regulator=CRP; target=yjcH; function=+
- `activates` --> [[gene.b4069|gene.b4069]] `RegulonDB` `C` - regulator=CRP; target=acs; function=+
- `activates` --> [[gene.b4111|gene.b4111]] `RegulonDB` `S` - regulator=CRP; target=proP; function=-+
- `activates` --> [[gene.b4118|gene.b4118]] `RegulonDB` `S` - regulator=CRP; target=melR; function=+
- `activates` --> [[gene.b4119|gene.b4119]] `RegulonDB` `S` - regulator=CRP; target=melA; function=+
- `activates` --> [[gene.b4120|gene.b4120]] `RegulonDB` `S` - regulator=CRP; target=melB; function=+
- `activates` --> [[gene.b4124|gene.b4124]] `RegulonDB` `S` - regulator=CRP; target=dcuR; function=+
- `activates` --> [[gene.b4193|gene.b4193]] `RegulonDB` `S` - regulator=CRP; target=ulaA; function=+
- `activates` --> [[gene.b4194|gene.b4194]] `RegulonDB` `S` - regulator=CRP; target=ulaB; function=+
- `activates` --> [[gene.b4195|gene.b4195]] `RegulonDB` `S` - regulator=CRP; target=ulaC; function=+
- `activates` --> [[gene.b4196|gene.b4196]] `RegulonDB` `S` - regulator=CRP; target=ulaD; function=+
- `activates` --> [[gene.b4197|gene.b4197]] `RegulonDB` `S` - regulator=CRP; target=ulaE; function=+
- `activates` --> [[gene.b4198|gene.b4198]] `RegulonDB` `S` - regulator=CRP; target=ulaF; function=+
- `activates` --> [[gene.b4200|gene.b4200]] `RegulonDB` `S` - regulator=CRP; target=rpsF; function=+
- `activates` --> [[gene.b4201|gene.b4201]] `RegulonDB` `S` - regulator=CRP; target=priB; function=+
- `activates` --> [[gene.b4202|gene.b4202]] `RegulonDB` `S` - regulator=CRP; target=rpsR; function=+
- `activates` --> [[gene.b4203|gene.b4203]] `RegulonDB` `S` - regulator=CRP; target=rplI; function=+
- `activates` --> [[gene.b4208|gene.b4208]] `RegulonDB` `C` - regulator=CRP; target=cycA; function=+
- `activates` --> [[gene.b4213|gene.b4213]] `RegulonDB` `S` - regulator=CRP; target=cpdB; function=+
- `activates` --> [[gene.b4217|gene.b4217]] `RegulonDB` `C` - regulator=CRP; target=ytfK; function=+
- `activates` --> [[gene.b4300|gene.b4300]] `RegulonDB` `S` - regulator=CRP; target=sgcR; function=+
- `activates` --> [[gene.b4301|gene.b4301]] `RegulonDB` `S` - regulator=CRP; target=sgcE; function=+
- `activates` --> [[gene.b4302|gene.b4302]] `RegulonDB` `S` - regulator=CRP; target=sgcA; function=+
- `activates` --> [[gene.b4303|gene.b4303]] `RegulonDB` `S` - regulator=CRP; target=sgcQ; function=+
- `activates` --> [[gene.b4304|gene.b4304]] `RegulonDB` `S` - regulator=CRP; target=sgcC; function=+
- `activates` --> [[gene.b4305|gene.b4305]] `RegulonDB` `S` - regulator=CRP; target=sgcX; function=+
- `activates` --> [[gene.b4309|gene.b4309]] `RegulonDB` `S` - regulator=CRP; target=nanS; function=+
- `activates` --> [[gene.b4310|gene.b4310]] `RegulonDB` `S` - regulator=CRP; target=nanM; function=+
- `activates` --> [[gene.b4311|gene.b4311]] `RegulonDB` `S` - regulator=CRP; target=nanC; function=+
- `activates` --> [[gene.b4322|gene.b4322]] `RegulonDB` `S` - regulator=CRP; target=uxuA; function=+
- `activates` --> [[gene.b4354|gene.b4354]] `RegulonDB` `S` - regulator=CRP; target=btsT; function=+
- `activates` --> [[gene.b4381|gene.b4381]] `RegulonDB` `C` - regulator=CRP; target=deoC; function=-+
- `activates` --> [[gene.b4382|gene.b4382]] `RegulonDB` `C` - regulator=CRP; target=deoA; function=-+
- `activates` --> [[gene.b4383|gene.b4383]] `RegulonDB` `C` - regulator=CRP; target=deoB; function=-+
- `activates` --> [[gene.b4384|gene.b4384]] `RegulonDB` `C` - regulator=CRP; target=deoD; function=-+
- `activates` --> [[gene.b4426|gene.b4426]] `RegulonDB` `S` - regulator=CRP; target=mcaS; function=+
- `activates` --> [[gene.b4438|gene.b4438]] `RegulonDB` `C` - regulator=CRP; target=cyaR; function=+
- `activates` --> [[gene.b4460|gene.b4460]] `RegulonDB` `C` - regulator=CRP; target=araH; function=+
- `activates` --> [[gene.b4471|gene.b4471]] `RegulonDB` `C` - regulator=CRP; target=tdcG; function=+
- `activates` --> [[gene.b4476|gene.b4476]] `RegulonDB` `S` - regulator=CRP; target=gntU; function=+
- `activates` --> [[gene.b4477|gene.b4477]] `RegulonDB` `C` - regulator=CRP; target=dgoA; function=+
- `activates` --> [[gene.b4478|gene.b4478]] `RegulonDB` `C` - regulator=CRP; target=dgoD; function=+
- `activates` --> [[gene.b4479|gene.b4479]] `RegulonDB` `C` - regulator=CRP; target=dgoR; function=+
- `activates` --> [[gene.b4565|gene.b4565]] `RegulonDB` `S` - regulator=CRP; target=sgcB; function=+
- `activates` --> [[gene.b4725|gene.b4725]] `RegulonDB` `S` - regulator=CRP; target=rseD; function=+
- `activates` --> [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=CRP; target=sdhX; function=+
- `activates` --> [[gene.b4805|gene.b4805]] `RegulonDB` `S` - regulator=CRP; target=raiZ; function=+
- `activates` --> [[gene.b4807|gene.b4807]] `RegulonDB` `C` - regulator=CRP; target=malH; function=+
- `activates` --> [[gene.b4829|gene.b4829]] `RegulonDB` `C` - regulator=CRP; target=uhpU; function=+
- `is_component_of` --> [[complex.ecocyc.CPLX0-8312|complex.ecocyc.CPLX0-8312]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.PC00004|complex.ecocyc.PC00004]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `represses` --> [[gene.b0124|gene.b0124]] `RegulonDB` `C` - regulator=CRP; target=gcd; function=-
- `represses` --> [[gene.b0342|gene.b0342]] `RegulonDB` `C` - regulator=CRP; target=lacA; function=-+
- `represses` --> [[gene.b0343|gene.b0343]] `RegulonDB` `S` - regulator=CRP; target=lacY; function=-+
- `represses` --> [[gene.b0344|gene.b0344]] `RegulonDB` `C` - regulator=CRP; target=lacZ; function=-+
- `represses` --> [[gene.b0396|gene.b0396]] `RegulonDB` `S` - regulator=CRP; target=araJ; function=-+
- `represses` --> [[gene.b0411|gene.b0411]] `RegulonDB` `C` - regulator=CRP; target=tsx; function=-+
- `represses` --> [[gene.b0675|gene.b0675]] `RegulonDB` `S` - regulator=CRP; target=umpH; function=-+
- `represses` --> [[gene.b0676|gene.b0676]] `RegulonDB` `S` - regulator=CRP; target=nagC; function=-+
- `represses` --> [[gene.b0677|gene.b0677]] `RegulonDB` `S` - regulator=CRP; target=nagA; function=-+
- `represses` --> [[gene.b0678|gene.b0678]] `RegulonDB` `S` - regulator=CRP; target=nagB; function=-+
- `represses` --> [[gene.b0679|gene.b0679]] `RegulonDB` `C` - regulator=CRP; target=nagE; function=-+
- `represses` --> [[gene.b0756|gene.b0756]] `RegulonDB` `S` - regulator=CRP; target=galM; function=-+
- `represses` --> [[gene.b0757|gene.b0757]] `RegulonDB` `S` - regulator=CRP; target=galK; function=-+
- `represses` --> [[gene.b0758|gene.b0758]] `RegulonDB` `S` - regulator=CRP; target=galT; function=-+
- `represses` --> [[gene.b0759|gene.b0759]] `RegulonDB` `S` - regulator=CRP; target=galE; function=-+
- `represses` --> [[gene.b0907|gene.b0907]] `RegulonDB` `S` - regulator=CRP; target=serC; function=-
- `represses` --> [[gene.b0908|gene.b0908]] `RegulonDB` `S` - regulator=CRP; target=aroA; function=-
- `represses` --> [[gene.b1111|gene.b1111]] `RegulonDB` `S` - regulator=CRP; target=comR; function=-
- `represses` --> [[gene.b1112|gene.b1112]] `RegulonDB` `S` - regulator=CRP; target=bhsA; function=-
- `represses` --> [[gene.b1189|gene.b1189]] `RegulonDB` `S` - regulator=CRP; target=dadA; function=-+
- `represses` --> [[gene.b1190|gene.b1190]] `RegulonDB` `S` - regulator=CRP; target=dadX; function=-+
- `represses` --> [[gene.b1256|gene.b1256]] `RegulonDB` `S` - regulator=CRP; target=ompW; function=-
- `represses` --> [[gene.b1445|gene.b1445]] `RegulonDB` `S` - regulator=CRP; target=ortT; function=-
- `represses` --> [[gene.b1620|gene.b1620]] `RegulonDB` `C` - regulator=CRP; target=malI; function=-+
- `represses` --> [[gene.b2143|gene.b2143]] `RegulonDB` `C` - regulator=CRP; target=cdd; function=-+
- `represses` --> [[gene.b2415|gene.b2415]] `RegulonDB` `S` - regulator=CRP; target=ptsH; function=-+
- `represses` --> [[gene.b2416|gene.b2416]] `RegulonDB` `S` - regulator=CRP; target=ptsI; function=-+
- `represses` --> [[gene.b2417|gene.b2417]] `RegulonDB` `S` - regulator=CRP; target=crr; function=-+
- `represses` --> [[gene.b2509|gene.b2509]] `RegulonDB` `C` - regulator=CRP; target=xseA; function=-
- `represses` --> [[gene.b2741|gene.b2741]] `RegulonDB` `S` - regulator=CRP; target=rpoS; function=-
- `represses` --> [[gene.b2754|gene.b2754]] `RegulonDB` `S` - regulator=CRP; target=cas2; function=-
- `represses` --> [[gene.b2755|gene.b2755]] `RegulonDB` `S` - regulator=CRP; target=cas1; function=-
- `represses` --> [[gene.b2756|gene.b2756]] `RegulonDB` `S` - regulator=CRP; target=casE; function=-
- `represses` --> [[gene.b2757|gene.b2757]] `RegulonDB` `S` - regulator=CRP; target=casD; function=-
- `represses` --> [[gene.b2758|gene.b2758]] `RegulonDB` `S` - regulator=CRP; target=casC; function=-
- `represses` --> [[gene.b2759|gene.b2759]] `RegulonDB` `S` - regulator=CRP; target=casB; function=-
- `represses` --> [[gene.b2760|gene.b2760]] `RegulonDB` `S` - regulator=CRP; target=casA; function=-
- `represses` --> [[gene.b2964|gene.b2964]] `RegulonDB` `C` - regulator=CRP; target=nupG; function=-+
- `represses` --> [[gene.b3164|gene.b3164]] `RegulonDB` `C` - regulator=CRP; target=pnp; function=-
- `represses` --> [[gene.b3165|gene.b3165]] `RegulonDB` `C` - regulator=CRP; target=rpsO; function=-
- `represses` --> [[gene.b3166|gene.b3166]] `RegulonDB` `C` - regulator=CRP; target=truB; function=-
- `represses` --> [[gene.b3167|gene.b3167]] `RegulonDB` `C` - regulator=CRP; target=rbfA; function=-
- `represses` --> [[gene.b3168|gene.b3168]] `RegulonDB` `C` - regulator=CRP; target=infB; function=-
- `represses` --> [[gene.b3169|gene.b3169]] `RegulonDB` `C` - regulator=CRP; target=nusA; function=-
- `represses` --> [[gene.b3170|gene.b3170]] `RegulonDB` `C` - regulator=CRP; target=rimP; function=-
- `represses` --> [[gene.b3171|gene.b3171]] `RegulonDB` `C` - regulator=CRP; target=metY; function=-
- `represses` --> [[gene.b3212|gene.b3212]] `RegulonDB` `C` - regulator=CRP; target=gltB; function=-
- `represses` --> [[gene.b3213|gene.b3213]] `RegulonDB` `C` - regulator=CRP; target=gltD; function=-
- `represses` --> [[gene.b3214|gene.b3214]] `RegulonDB` `C` - regulator=CRP; target=gltF; function=-
- `represses` --> [[gene.b3230|gene.b3230]] `RegulonDB` `S` - regulator=CRP; target=rpsI; function=-
- `represses` --> [[gene.b3231|gene.b3231]] `RegulonDB` `S` - regulator=CRP; target=rplM; function=-
- `represses` --> [[gene.b3356|gene.b3356]] `RegulonDB` `C` - regulator=CRP; target=yhfA; function=-+
- `represses` --> [[gene.b3357|gene.b3357]] `RegulonDB` `C` - regulator=CRP; target=crp; function=-+
- `represses` --> [[gene.b3363|gene.b3363]] `RegulonDB` `S` - regulator=CRP; target=ppiA; function=-+
- `represses` --> [[gene.b3403|gene.b3403]] `RegulonDB` `S` - regulator=CRP; target=pck; function=-+
- `represses` --> [[gene.b3404|gene.b3404]] `RegulonDB` `C` - regulator=CRP; target=envZ; function=-+
- `represses` --> [[gene.b3405|gene.b3405]] `RegulonDB` `C` - regulator=CRP; target=ompR; function=-+
- `represses` --> [[gene.b3461|gene.b3461]] `RegulonDB` `S` - regulator=CRP; target=rpoH; function=-+
- `represses` --> [[gene.b3512|gene.b3512]] `RegulonDB` `S` - regulator=CRP; target=gadE; function=-
- `represses` --> [[gene.b3513|gene.b3513]] `RegulonDB` `S` - regulator=CRP; target=mdtE; function=-
- `represses` --> [[gene.b3514|gene.b3514]] `RegulonDB` `S` - regulator=CRP; target=mdtF; function=-
- `represses` --> [[gene.b3574|gene.b3574]] `RegulonDB` `S` - regulator=CRP; target=plaR; function=-
- `represses` --> [[gene.b3781|gene.b3781]] `RegulonDB` `S` - regulator=CRP; target=trxA; function=-
- `represses` --> [[gene.b3806|gene.b3806]] `RegulonDB` `S` - regulator=CRP; target=cyaA; function=-
- `represses` --> [[gene.b3831|gene.b3831]] `RegulonDB` `C` - regulator=CRP; target=udp; function=-+
- `represses` --> [[gene.b3884|gene.b3884]] `RegulonDB` `S` - regulator=CRP; target=csqR; function=-+
- `represses` --> [[gene.b3934|gene.b3934]] `RegulonDB` `S` - regulator=CRP; target=cytR; function=-+
- `represses` --> [[gene.b4030|gene.b4030]] `RegulonDB` `S` - regulator=CRP; target=psiE; function=-
- `represses` --> [[gene.b4111|gene.b4111]] `RegulonDB` `S` - regulator=CRP; target=proP; function=-+
- `represses` --> [[gene.b4172|gene.b4172]] `RegulonDB` `S` - regulator=CRP; target=hfq; function=-
- `represses` --> [[gene.b4173|gene.b4173]] `RegulonDB` `S` - regulator=CRP; target=hflX; function=-
- `represses` --> [[gene.b4174|gene.b4174]] `RegulonDB` `S` - regulator=CRP; target=hflK; function=-
- `represses` --> [[gene.b4175|gene.b4175]] `RegulonDB` `S` - regulator=CRP; target=hflC; function=-
- `represses` --> [[gene.b4381|gene.b4381]] `RegulonDB` `C` - regulator=CRP; target=deoC; function=-+
- `represses` --> [[gene.b4382|gene.b4382]] `RegulonDB` `C` - regulator=CRP; target=deoA; function=-+
- `represses` --> [[gene.b4383|gene.b4383]] `RegulonDB` `C` - regulator=CRP; target=deoB; function=-+
- `represses` --> [[gene.b4384|gene.b4384]] `RegulonDB` `C` - regulator=CRP; target=deoD; function=-+
- `represses` --> [[gene.b4457|gene.b4457]] `RegulonDB` `S` - regulator=CRP; target=csrC; function=-
- `represses` --> [[gene.b4718|gene.b4718]] `RegulonDB` `S` - regulator=CRP; target=gadF; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b3357|gene.b3357]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACJ8`
- `KEGG:ecj:JW5702;eco:b3357;ecoc:C3026_18235;`
- `GeneID:86862244;93122175;947867;`
- `GO:GO:0003680; GO:0003700; GO:0005829; GO:0006351; GO:0008301; GO:0030552; GO:0032993; GO:0042802; GO:0043565; GO:0045013; GO:0045892; GO:0045893`

## Notes

DNA-binding transcriptional dual regulator CRP (Catabolite activator protein) (CAP) (Catabolite gene activator) (cAMP receptor protein) (CRP) (cAMP regulatory protein) (cAMP-activated global transcriptional regulator CRP)
